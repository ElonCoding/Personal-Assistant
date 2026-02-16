# Personal-Assistant (Jarvis)

**Jarvis** is a voice-enabled, intelligent personal assistant framework built on top of
[`livekit`](https://github.com/livekit) agents and various helper tools. Designed and
coded by Shashank Sir (as per prompts), it can control the system, search the internet,
fetch weather, open files, and interact with the user in natural Hinglish. A separate
Pygame animation for Republic Day celebration is also included for demonstration.

---

## 🧠 Core Features

- ✅ Real‑time voice assistant using LiveKit/Google GenAI
- 🔧 A rich set of tools for system control (shutdown, lock, app launch, etc.)
- 🌐 Internet search via Google Custom Search API
- ☁ Weather reports using OpenWeather API
- 📁 File indexing and opening (search across drives)
- 🖱 Keyboard/mouse automation
- 🧠 Memory subsystem for conversation history
- ✍️ LangChain-based reasoning tool for generative tasks
- 🎨 Pygame visualisation (`republic_day.py`) as a fun side project

---

## 📁 Repository Structure

```
Personal-Assistant/
├─ agent.py              # Primary LiveKit agent entrypoint
├─ brain.py              # Alternate agent with memory extractor
├─ jarvis_prompt.py      # System prompts & language rules (Hindi+English mix)
├─ jarvis_search.py      # Internet search & datetime utilities
├─ jarvis_get_weather.py # Weather querying tool
├─ jarvis_ctrl_window.py # Windows-specific control tools (apps, shutdown etc.)
├─ Jarvis_file_opner.py  # File‑search/opening utility using fuzzy matching
├─ jarvis_reasoning.py   # LangChain "thinking" agent + reasoning tool
├─ keyboard_mouse_control.py # Cursor & keyboard control tools
├─ memory_store.py       # Persistent conversation memory manager
├─ memory_loop.py        # Background loop for saving chat history
├─ republic_day.py       # Pygame animation (republic day celebration)
├─ requirement.txt       # Python dependencies
└─ run_agent.bat         # Windows batch script to start the assistant
```

> Note: most modules use `@function_tool` decorator from livekit to expose
tools to the agent runtime.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Windows 10/11 (some control tools leverage `shutdown`, `netsh`, etc.)
- A [LiveKit](https://livekit.io/) environment or account
- Google GenAI credentials (via `livekit.plugins.google`)
- API keys in `.env` file:
  ```ini
  GOOGLE_SEARCH_API_KEY=...
  SEARCH_ENGINE_ID=...
  OPENWEATHER_API_KEY=...
  # plus any LiveKit-specific keys (e.g. PROJECT_KEY/SECRET)
  ```

> If you run on Linux/Mac, many system‑control functions are no‑ops or will fail;
> you'll need to adapt them accordingly.

### Installation

```bash
cd Personal-Assistant/Personal-Assistant
python -m venv venv            # create virtualenv
source venv/bin/activate       # (or .\venv\Scripts\activate on Windows)
pip install -r requirement.txt
```

### Running the assistant

- **Via Python script:**
  ```bash
  python agent.py    # starts the voice‑enabled agent
  # or
  python brain.py    # variant with chat context memory extractor
  ```

- **Quick start (Windows):**
  Double‑click `run_agent.bat` or run it from a terminal. It wraps the above.

Once running, speak to Jarvis through the LiveKit room; the agent uses Google
`charon` voice model and responds using natural Hinglish.

### Using the tools

Jarvis understands spoken requests and will call the appropriate tools when you
ask. Examples:

- _"खिड़की बंद करो"_ → `close_application`
- _"मौसम बताओ दिल्ली का"_ → `get_weather`
- _"Google पर Python के बारे में search करो"_ → `search_internet`
- _"D drive से resume खोलो"_ → `Play_file`
- _"माउस को X पर ले जाओ"_ → `move_cursor_tool`

The prompt rules (`jarvis_prompt.py`) enforce Hinglish responses, date/city context,
and tool‑first behaviour.

---

## 🛠 Development Notes

- Tools are exposed using `@function_tool` so the LiveKit agent can call them
  with structured arguments.
- `keyboard_mouse_control.py` provides generic cursor and keyboard actions for
  automation workflows.
- `jarvis_reasoning.py` demonstrates integrating LangChain REACT agents for
  advanced query handling and dynamic planning.
- `memory_store.py` keeps a JSON log of conversations; the helper loop
  (`memory_loop.py`) periodically saves new messages.
- `republic_day.py` is largely independent and can be run with `python
  republic_day.py` to see an animation.

---

## ✅ Testing & Logging

- Modules generally log to console using `logging` at `INFO` level.
- Add or adjust loggers as needed when debugging tools or memory behaviour.

## 📦 Dependencies

See `Personal-Assistant/requirement.txt`. Key packages include:

- `livekit` and `livekit-agents`
- `requests`, `dotenv`, `psutil`, `opencv-python` (optional)
- `langchain-google-genai`, `fuzzywuzzy`, `pygetwindow`, `pygame`

---

## 📝 License

This project uses the [MIT License](LICENSE).

---

## 💡 Contributions

Feel free to fork or adapt the assistant for your own use case. Add more tools,
enhance prompts, or port to other OSes.

> 🙏 Thank you for exploring Jarvis! Keep your workspace organized and voice-enabled.