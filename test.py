# from pynput import keyboard

# ctrl_held = False

# def on_press(key):
#     global ctrl_held
#     try:
#         if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
#             ctrl_held = True
#         elif key.char.lower() == 'm' and ctrl_held:
#             print("Ctrl + M detected!")
#     except AttributeError:
#         pass

# def on_release(key):
#     global ctrl_held
#     if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
#         ctrl_held = False

# listener = keyboard.Listener(on_press=on_press, on_release=on_release)
# listener.start()

# # Keep the script alive
# try:
#     while True:
#         pass
# except KeyboardInterrupt:
#     print("Stopped by user")

# def on_press(key):
#     print(f"Pressed: {key}")

#note to myself : previous one failed xoxo
# import keyboard

# def listen_hotkey():
#     print("Listening for Ctrl + M...")

#     keyboard.add_hotkey('ctrl+m', lambda: print("✅ Ctrl + M detected!"))

#     keyboard.wait('esc')  

# listen_hotkey()

# import winreg

# key_path = r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders"
# with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path) as key:
#     desktop_path, _ = winreg.QueryValueEx(key, "Desktop")
# print(desktop_path)  # this will be TrashDesk

import os, winreg

key_path = r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders"
with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path) as key:
    desktop_path, _ = winreg.QueryValueEx(key, "Desktop")

desktop_path = os.path.expandvars(desktop_path)  # resolves %USERPROFILE%
print(desktop_path)  # C:\Users\Asahi\TrashDesk
