"""
speech.py
Speech recognition (STT) and TTS helper functions.
"""

import pyttsx3
import speech_recognition as sr
from typing import Optional

# TTS setup
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

def speak(text: str):
    """Speak text aloud and print it."""
    if not text:
        return
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def wish_me():
    import datetime
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("Ready to comply. What can I do for you?")

def take_command(timeout: int = 6, phrase_time_limit: int = 8) -> str:
    """
    Listen from microphone and return recognized text.
    Returns "None" string on failure to keep compatibility with existing code.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        except sr.WaitTimeoutError:
            print("Timeout waiting for command.")
            return "None"

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        return query
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return "None"
    except Exception as e:
        print("Speech recognition error:", e)
        return "None"
