
<h1 align="center">🤖 Bantu AI - Personal Desktop Assistant</h1>
<p align="center">
  <img src="https://media.giphy.com/media/l0HUpt2s9Pclgt9Vm/giphy.gif" width="400"/>
</p>

> **Inspired by J.A.R.V.I.S.** – Built for the real world.  
> Bantu AI is a smart, Python-powered desktop assistant with voice control, GUI interface, and AI intelligence – designed to assist you like a true digital partner.

---

## 🧠 Features

- 🎙️ **Voice Command Recognition**  
- 🧾 **Chat Memory** for continuous, context-aware interaction  
- 🌐 **Browser Control** using voice (open websites, search the web, etc.)  
- 💬 **AI Responses** powered by **Cohere API** + **Groq API**  
- 🖥️ **Tkinter GUI** – Lightweight and elegant desktop interface  
- ⚡ **Asynchronous Processing** for smooth multitasking  
- 🎯 Built with productivity and personalization in mind

---

## 🛠️ Tech Stack

| Layer       | Technology          |
|-------------|---------------------|
| Language    | Python 🐍           |
| UI          | Tkinter 🖼️          |
| AI Engine   | Cohere & Groq APIs  |
| Voice Input | SpeechRecognition 🎤 |
| Output      | pyttsx3 (Text to Speech) 🗣️ |
| Async Ops   | asyncio, threading ⚡ |

---

## 🚀 Getting Started

> 🧑‍💻 Clone the repo and install the dependencies:

```bash
git clone https://github.com/harsh4dev/bantuai.git
cd bantu-ai
pip install -r requirements.txt
```

> ⚙️ Add your API keys (Cohere, Groq, etc.) in a `.env` file or directly in config block.

---

## 🕹️ How to Use

1. **Run the assistant**  
   ```bash
   python main.py
   ```

2. **Use the GUI** or activate voice commands:  
   - “Open YouTube”  
   - “Search for Python tutorials”  
   - “Tell me a joke”  
   - “What’s the time?”

3. **Chat with Memory**  
   Bantu AI remembers context within a session, just like JARVIS would.

---

## 🧪 Demo 

> 🎥 YouTube demo and walkthrough is uploaded on [Techy Guy](https://www.youtube.com/@TechyGuynp)

---

## 💡 Inspiration

> This project was inspired by **J.A.R.V.I.S.**, Tony Stark’s legendary AI assistant from the Marvel universe.  
> Bantu AI brings that dream closer to reality using accessible open-source tools and modern AI APIs.

---

## 📁 Project Structure

```
bantu-ai/
├── Backend/           # Main Logic, voice chat memory
├── Data/              # Chat History
├── Frontend/            # contains graphics and GUI codes by tkinter
├── .env              # API keys (not included)
├── requirements.txt
└── main.py          # Entry point
```

---

## 🤝 Contributing

Have ideas or improvements? Open an issue or pull request – let's evolve Bantu AI together!

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

<p align="center">
  <img src="https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif" width="350"/>
</p>

> **“Sir, Bantu is online.”**
