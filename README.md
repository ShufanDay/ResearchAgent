
<div align="center">

<h1>🔬 ResearchAgent</h1>

<h3>A Lightweight Research Agent Framework Built from Scratch</h3>




<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/OpenAI-Compatible-412991?style=for-the-badge&logo=openai">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Version-v0.1.0-blue?style=for-the-badge">
</p>
Work in progress !
</div>

---

# ✨ Overview

ResearchAgent is a lightweight Agent Framework designed for AI research. Unlike frameworks such as LangChain or LangGraph, ResearchAgent is implemented completely from scratch to help developers understand the internal workflow of modern AI Agents.

The long-term goal of this project is to build an extensible research platform that supports:

- 📄 Paper Reading
- 🔍 Paper Search
- 🧠 Memory
- 📚 RAG
- 🤖 Multi-Agent
- 💻 Code Agent
- 📝 Paper Writing Assistant

---

# 🏗 Architecture

```text
                User
                  │
                  ▼
            ResearchAgent
                  │
        ┌─────────┴─────────┐
        │                   │
      Planner            Memory
        │                   │
        └─────────┬─────────┘
                  ▼
             Tool Registry
                  │
     ┌────────────┼────────────┐
     ▼            ▼            ▼
 PDF Tool     Search Tool   Python Tool
                  │
                  ▼
                LLM
```

---

# 🚀 Features
* ✅ ReAct Agent
* ✅ Tool Calling
* ✅ Tool Registry
* ✅ Modular Architecture
* 🚧 Memory
* 🚧 Planner
* 🚧 Reflection
* 🚧 RAG
* 🚧 Multi-Agent

---
# 📂 Project Structure
```text
ResearchAgent
│
├── app
│   ├── core
│   ├── llm
│   ├── tools
│   ├── planner
│   ├── memory
│   └── prompt
│
├── data
│
├── tests
│
└── main.py
```
---
# ⚡ Quick Start

Clone the project

```bash
git clone https://github.com/yourname/ResearchAgent.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Configure environment

```bash
cp .env.example .env
```

Run

```bash
python main.py
```

---

# 🛣 Roadmap

| Version | Features           |
| ------- | ------------------ |
| v0.1    | Basic ReAct Agent  |
| v0.2    | Tool Registry      |
| v0.3    | Prompt Builder     |
| v0.4    | Action Model       |
| v0.5    | Memory             |
| v0.6    | Planner            |
| v0.7    | Reflection         |
| v0.8    | RAG                |
| v0.9    | Multi-Agent        |
| v1.0    | Research Assistant |

---

# 🎯 Vision

ResearchAgent aims to become an educational and research-oriented Agent Framework.

Instead of hiding implementation details behind complex abstractions, every module is implemented from scratch so that researchers can easily understand, modify and extend the system.

---

# 🤝 Contributing

Contributions are welcome!

Feel free to submit Issues and Pull Requests.

---

# 📄 License

MIT License.

---


## ⭐ Star History

If this project has been useful to you, a ⭐ would be greatly appreciated!
