import speech_recognition as sr
from core.chatgpt_api import send_to_chatgpt

recognizer = sr.Recognizer()

def activate_miya_listener():
    print("🎤 Miya is now listening...")
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.4)
        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=5
            )
        except sr.WaitTimeoutError:
            print("⏱️ Miya is ignoring you.")
            return
    try:
        user_text = recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        print("❌ Miya heard nothing understandable.")
        return
    except sr.RequestError:
        print("⏱️ Miya is ignoring you.")  # google busy
        return
    user_text = user_text.strip()
    print(f"🧠 You said: \"{user_text}\"")

    if not user_text:
        print("⚠️ Miya is ignoring you.")
        return
    if user_text.lower().startswith("open"):
        print("🗂️ Command detected!")
        print(f"➡️ Handling OPEN command: {user_text}")
    else:
        print("💬 Conversation detected — sending to ChatGPT...")
        send_to_chatgpt(user_text)
