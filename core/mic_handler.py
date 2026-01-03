import speech_recognition as sr
import os
from core.chatgpt_api import send_to_chatgpt
from vosk import Model, KaldiRecognizer
import json
import sys
import wave
import urllib.request

recognizer = sr.Recognizer()

def internet_available():
    try:
        urllib.request.urlopen("http://google.com", timeout=2)
        return True
    except:
        return False

VOSK_MODEL_PATH = os.path.join("models", "vosk")
vosk_model = None
if os.path.exists(VOSK_MODEL_PATH):
    vosk_model = Model(VOSK_MODEL_PATH)

def activate_miya_listener():
    use_google = internet_available() and vosk_model is not None

    model_name = "(Google)" if use_google else "(Vosk)"
    print(f"🎤 Miya is now listening... {model_name}")
    
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.4)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            print(f"⏱️ Miya is ignoring you. {model_name}")
            return

    if use_google:
        try:
            user_text = recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            print(f"Miya heard nothing understandable. {model_name}")
            return
        except sr.RequestError:
            print(f"Miya is ignoring you. {model_name}")  # Google busy
            return

        user_text = user_text.strip()
        print(f"You said: \"{user_text}\" {model_name}")

        if not user_text:
            print(f"Miya is ignoring you. {model_name}")
            return

        if user_text.lower().startswith("open"):
            print(f"Command detected! {model_name}")
            print(f"Handling OPEN command: {user_text} {model_name}")
        else:
            print(f"Conversation detected — sending to ChatGPT... {model_name}")
            send_to_chatgpt(user_text)

    else:
        try:
            wav_path = "temp_audio.wav"
            with open(wav_path, "wb") as f:
                f.write(audio.get_wav_data())

            wf = wave.open(wav_path, "rb")
            rec = KaldiRecognizer(vosk_model, wf.getframerate())
            rec.SetWords(True)

            results = []
            while True:
                data = wf.readframes(4000)
                if len(data) == 0:
                    break
                if rec.AcceptWaveform(data):
                    res = json.loads(rec.Result())
                    results.append(res.get("text", ""))

            results.append(json.loads(rec.FinalResult()).get("text", ""))
            user_text = " ".join(results).strip()
            wf.close()
            os.remove(wav_path)

        except Exception as e:
            print(f"Miya flicked her tail at you. (Vosk error: {e}) {model_name}")
            return

        if not user_text:
            print(f"Miya flicked her tail at you. {model_name}")
            return

        print(f"You said (offline): \"{user_text}\" {model_name}")
        if user_text.lower().startswith("open"):
            print(f"Command detected! {model_name}")
            print(f"Handling OPEN command: {user_text} {model_name}")
        else:
            print(f"Miya flicked her tail at you. {model_name}")  
