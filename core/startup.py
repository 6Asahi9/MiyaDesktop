import os
import sys
import winreg  

APP_NAME = "MiyaDesktop"

def toggle_startup(is_on: bool):
    if getattr(sys, 'frozen', False):
        app_path = sys.executable
    else:
        app_path = os.path.abspath(sys.argv[0])

    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Run",
        0,
        winreg.KEY_WRITE
    )

    if is_on:
        winreg.SetValueEx(key, APP_NAME, 0, winreg.REG_SZ, f'"{app_path}"')
        print("Startup on")
    else:
        try:
            winreg.DeleteValue(key, APP_NAME)
            print("Startup off")
        except FileNotFoundError:
            pass  
    winreg.CloseKey(key)
