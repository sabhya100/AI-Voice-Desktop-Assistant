"""
actions.py
All helper functions that perform OS / GUI / Browser actions.
Note: Many GUI actions (pyautogui) are screen-resolution and OS dependent.
"""

import webbrowser
import os
import pyautogui
import time
import subprocess
from typing import Optional, Tuple

# WARNING: coordinates in this file are placeholders — machine-dependent.
# Replace with image-based locateCenterOnScreen or configurable values.

def open_website(query: str):
    # expects something like "open youtube website" or "open google website"
    website_name = query.replace('open', '').replace('website', '').strip()
    if not website_name.startswith('http'):
        if '.' not in website_name:
            website_name += '.com'
        website_name = 'https://' + website_name
    webbrowser.open(website_name)
    print(f"Opening {website_name}")

def open_youtube():
    webbrowser.open("https://youtube.com")

def search_in_youtube():
    # fragile: assumes a browser is open and search box coords match
    pyautogui.click(x=800, y=130, clicks=1)

def search_in_google():
    pyautogui.click(x=800, y=480, clicks=1)

def type_text(text: str):
    pyautogui.typewrite(text)
    pyautogui.press("enter")

def click_coords(x: Optional[int], y: Optional[int], clicks: int = 1, interval: float = 0, button: str = 'left', hotkey: Optional[Tuple[str,...]] = None, special: Optional[str] = None):
    if hotkey:
        pyautogui.hotkey(*hotkey)
        return
    if special == 'open_pc':
        # try to locate image; expects 'ss1.png' placed in repo
        try:
            img = pyautogui.locateCenterOnScreen('ss1.png', confidence=0.3)
            if img:
                pyautogui.doubleClick(img)
        except Exception as e:
            print("Open PC: image locate failed:", e)
        return
    if x is None or y is None:
        return
    pyautogui.click(x=x, y=y, clicks=clicks, interval=interval, button=button)

def open_presentation(path: str = r"C:\Users\sabhya100\Desktop\AI Voice assistant.pptx"):
    try:
        os.startfile(path)
    except Exception as e:
        print("Open presentation error:", e)

def open_cmd():
    try:
        subprocess.Popen("start cmd.exe", shell=True)
    except Exception as e:
        print("Open cmd error:", e)

def close_cmd():
    try:
        os.system("taskkill /f /im cmd.exe")
    except Exception as e:
        print("Close cmd error:", e)

def open_camera():
    import cv2
    cap = cv2.VideoCapture(0)
    try:
        while True:
            ret, img = cap.read()
            if not ret:
                break
            cv2.imshow('Webcam', img)
            if cv2.waitKey(1) & 0xFF == 27:
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

def toggle_volume(action: str, steps: int = 1, do_scroll: bool = False):
    """
    action: 'up', 'down', 'mute'
    steps: how many keypresses
    do_scroll: if True, perform horizontal scroll instead of volume
    """
    if do_scroll:
        pyautogui.hscroll(-500 if action == 'down' else 500, steps)
        return

    key_map = {
        'up': 'volumeup',
        'down': 'volumedown',
        'mute': 'volumemute',
    }
    key = key_map.get(action, 'volumeup')
    for _ in range(steps):
        pyautogui.press(key)

def open_drive(letter: str = 'c'):
    # Example for Windows File Explorer
    try:
        if letter.lower() == 'c':
            pyautogui.doubleClick(650, 200)
        elif letter.lower() == 'd':
            pyautogui.doubleClick(900, 200)
    except Exception as e:
        print("Open drive error:", e)

def maximize_window():
    pyautogui.hotkey('alt', 'space')
    time.sleep(0.1)
    pyautogui.press('x')

def minimise_window():
    pyautogui.hotkey('alt', 'space')
    time.sleep(0.1)
    pyautogui.press('n')

def show_desktop():
    pyautogui.hotkey('winleft', 'd')
