"""
main.py
Entrypoint for the voice assistant.
"""

from speech import speak, take_command, wish_me
from actions import (
    open_website, open_youtube, search_in_youtube, search_in_google, type_text,
    click_coords, open_presentation, open_cmd, close_cmd, open_camera, toggle_volume,
    open_drive, maximize_window, minimise_window, show_desktop
)
from ai_chat import chat_with_ai
from utils import eval_binary_expr, get_operator_fn
import wikipedia
import time
import sys

def main_loop():
    wish_me()
    while True:
        query = take_command()
        if query == "None":
            continue
        query = query.lower().strip()

        if 'hello alex' in query:
            print("Hello sir")
            speak("Hello sir")

        elif "time" in query:
            from datetime import datetime
            time_now = datetime.now().strftime("%H:%M")
            speak(f"The time now is {time_now}")
            print(f"The time now is : {time_now}")

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            q = query.replace("wikipedia", "").strip()
            try:
                results = wikipedia.summary(q, sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)   # <-- fixed: speak the results
            except Exception as e:
                print("Wikipedia error:", e)
                speak("Sorry, I couldn't find information on Wikipedia for that query.")

        elif 'open youtube' in query:
            open_youtube()

        elif "search in youtube" in query:
            search_in_youtube()

        elif "search in google" in query:
            search_in_google()

        elif "type " in query:
            text = query.replace("type ", "", 1).strip()
            type_text(text)

        elif "close this window" in query:
            click_coords(1900, 10)

        elif "go back" in query:
            click_coords(50, 50)

        elif "scroll down" in query:
            # machine dependent
            toggle_volume('down', steps=1, do_scroll=True)

        elif "scroll up" in query:
            toggle_volume('up', steps=1, do_scroll=True)

        elif 'open google' in query:
            open_website('open google website')

        elif 'close this tab' in query:
            click_coords(None, None, hotkey=('ctrl', 'w'))

        elif 'open new tab' in query:
            click_coords(None, None, hotkey=('ctrl', 't'))

        elif 'open tab 1' in query:
            click_coords(None, None, hotkey=('ctrl', '1'))
        elif 'open tab 2' in query:
            click_coords(None, None, hotkey=('ctrl', '2'))
        elif 'open tab 3' in query:
            click_coords(None, None, hotkey=('ctrl', '3'))
        elif 'open tab 4' in query:
            click_coords(None, None, hotkey=('ctrl', '4'))
        elif 'open tab 5' in query:
            click_coords(None, None, hotkey=('ctrl', '5'))
        elif 'open previous tab' in query:
            click_coords(None, None, hotkey=('ctrl', '9'))

        elif 'open presentation' in query:
            open_presentation()

        elif 'open command' in query:
            open_cmd()

        elif 'close command' in query:
            close_cmd()

        elif 'first link' in query:
            click_coords(450, 250)

        elif 'blank document' in query:
            click_coords(500, 200)

        elif 'do not save' in query:
            click_coords(980, 570)

        elif 'save' in query:
            click_coords(900, 570)

        elif 'first video' in query:
            click_coords(450, 280)
        elif 'second video' in query:
            click_coords(450, 600)
        elif 'third video' in query:
            click_coords(450, 920)

        elif "open camera" in query:
            open_camera()

        elif "go to sleep" in query:
            speak('Alright then, I am switching off')
            break

        elif "calculate" in query:
            # listen again for the expression
            speak("Ready for calculation")
            expr = take_command()
            if expr == "None":
                speak("I did not hear the expression.")
                continue
            try:
                result = eval_binary_expr(*(expr.split()))
                print(f"Result: {result}")
                speak(f"Your result is {result}")
            except Exception as e:
                print("Calculation error:", e)
                speak("Sorry, I couldn't compute that expression.")

        elif "volume up" in query:
            toggle_volume('up', steps=10)

        elif "volume down" in query:
            toggle_volume('down', steps=10)

        elif "unmute" in query or "mute" in query:
            toggle_volume('mute')

        elif "open pc" in query:
            # this relies on a screenshot file 'ss1.png' in repo or a detection method
            click_coords(None, None, special='open_pc')

        elif "c drive" in query:
            open_drive('c')

        elif "d drive" in query:
            open_drive('d')

        elif "maximize this window" in query:
            maximize_window()

        elif "minimise this window" in query:
            minimise_window()

        elif "full" in query:
            click_coords(800, 500)

        elif 'open' in query and 'website' in query:
            open_website(query)

        elif 'desktop' in query:
            show_desktop()

        else:
            # fallback to AI chat
            reply = chat_with_ai(query)
            if reply:
                speak(reply)

if __name__ == "__main__":
    try:
        main_loop()
    except KeyboardInterrupt:
        print("Exiting...")
        sys.exit(0)
