## 🧠 Volex Code — CLI AI Code Agent (Gemini 2.0)

**Volex Code** is a command-line AI code assistant powered by Gemini 2.0 Flash via the Google AI API. It reads, writes, and interacts with code using programmable tools—strictly within the current working directory.

Designed as a learning probe, Volex explores how to wire up custom AI agents, tool integration, and safe execution boundaries under real-world LLM constraints.

---

### 🚀 Features

* 🤖 AI agent powered by **Gemini 2.0 Flash**
* 🛠️ Custom-defined **tools** for code manipulation
* 📁 **Scoped to current directory**—no access to files outside
* 🔍 Reads, analyzes, and writes code via CLI
* 🧪 Lightweight project for learning and experimentation

---

### 🔧 Stack

* Language: **Python**
* AI Model: **Gemini 2.0 Flash** (via Google AI Studio API)
* Interface: **Command-Line (CLI)**
* Dependencies: `google.generativeai`, `dotenv`, etc.

---

### 💡 Motivation

Volex was built as a way to deeply understand:

* How LLM agents invoke tools and manage control flow
* How to structure safe, contained CLI agents
* The Gemini API’s capabilities and limitations in a real use case

---

### 🛠 Setup

1. **Clone the repo**

```bash
git clone https://github.com/yourusername/volex-code.git
cd volex-code
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Configure API key**

Create a `.env` file in the root:

```env
GOOGLE_API_KEY=your_key_here
```

4. **Run the agent**

```bash
python main.py
```

---

### 🧩 How It Works

* You input a prompt describing what you want (e.g., “create a Python script that fetches weather data”).
* Gemini responds and may call a tool like `write_file` or `read_file`.
* All file operations are **restricted to the current folder** to maintain sandbox safety.
* The agent loops through reflection, reasoning, and action—until the task is done or you exit.

---

### ⚠️ Safety & Limitations

* ✅ **No file access outside the current folder**
* 🔒 Requires your **own Gemini API key**

---

### 🧱 Contribution Notes

The project is early-stage but open:

* Extend by adding tools (e.g., lint, test, run, format)
* Add multi-file project awareness
* Swap Gemini for other models (Claude, GPT-4, etc.)

No formal contribution flow—**fork it, build it**.

---

### 📘 License

MIT

---
