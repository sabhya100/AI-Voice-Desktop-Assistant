# 🎤 AI Desktop Voice Assistant — “Alex”

A fully functional **AI-powered desktop voice assistant** built in Python.  
Alex can understand voice commands, control your system, open applications, browse the web, perform calculations, run AI conversations using an LLM API, and automate tasks using PyAutoGUI.

This project demonstrates real-world application of:
- Speech Recognition  
- Text-to-Speech (TTS)  
- GUI automation  
- API-based AI chatbot integration  
- Command parsing & system automation  
- Voice-controlled desktop interactions  

---

## 🚀 Features

### 🎙️ Voice Interaction
- Wake words & conversation mode  
- Natural speech recognition (Google Speech API)  
- Responsive TTS using pyttsx3  

### 💻 System Automation
- Open/close applications (CMD, Explorer)  
- Volume up/down/mute  
- Minimize/maximize windows  
- Switch to desktop  
- Scroll, navigate, click, type  
- Open drives (C:, D:)  
- Automated UI clicks with PyAutoGUI  

### 🌐 Web & Search
- Open websites  
- Search on YouTube  
- Search on Google  
- Open YouTube videos  

### 🧠 AI Chat Functionality
- Uses OpenRouter + DeepSeek model  
- Handles any general conversation  
- Writes explanations, code, summaries, etc.  
- Integrated fallback if API fails  

### 📷 Extra Functionalities
- Open camera feed  
- Perform calculations via voice  
- Wikipedia lookup (speaks output)  
- Media control  

---

## 📂 Folder Structure

```text
alex-voice-assistant/
│
├── main.py              # Main execution loop (voice commands, routing)
├── speech.py            # Speech recognition + TTS
├── actions.py           # OS, browser, app control, PyAutoGUI automation
├── ai_chat.py           # Chatbot API connection (OpenRouter + DeepSeek)
├── utils.py             # Helper functions (cleaning, parsing, safe execution)
│
├── README.md            # Documentation
└── requirements.txt     # Python dependencies
```
## 🧠 File Responsibilities

```plaintext
main.py
    • Initializes the assistant
    • Listens for voice commands
    • Routes tasks to speech/actions/AI modules
    • Handles the main loop & fallback logic

speech.py
    • Handles microphone input
    • Converts speech → text
    • Text-to-speech (TTS) output
    • Manages noise thresholds & timeouts

actions.py
    • All PyAutoGUI controls
    • App launch / close automation
    • Window management (minimize, maximize, desktop)
    • Browser automation
    • Volume and media key actions

ai_chat.py
    • Handles API calls to OpenRouter
    • Sends user queries to the DeepSeek model
    • Processes & returns AI responses
    • Error handling for network/API issues

utils.py
    • Helper utilities
    • Query cleanup & formatting
    • Safe wrappers for repeated tasks
```
## 🛠️ Installation

```bash
pip install -r requirements.txt
```

**Dependencies include:**
- pyttsx3  
- SpeechRecognition  
- PyAutoGUI  
- OpenCV  
- wikipedia  
- requests  

---

## ▶️ Running the Assistant

```bash
python main.py
```

Speak commands such as:

- “Hello Alex”  
- “Open YouTube”  
- “Search in Google”  
- “Volume up”  
- “Tell me the time”  
- “Calculate 5 plus 7”  
- “Explain artificial intelligence”  
- “Open Instagram website”  
- “Go to desktop”  

---

## 🎯 Future Enhancements

- Add wake-word detection (Snowboy / Porcupine)  
- Add GUI dashboard  
- Add custom skills & plug-ins  
- Add multi-language speech support  

---

## 👤 Author

**Sabhya Malhotra**  
AI & Java Engineer



