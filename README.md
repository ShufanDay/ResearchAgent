
<div align="center">

<h1>🔬 ResearchAgent</h1>

<h3>A Lightweight Research Agent Framework Built from Scratch</h3>

<p>从零开始构建的科研智能体框架</p>


<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/OpenAI-Compatible-412991?style=for-the-badge&logo=openai">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Version-v0.1.0-blue?style=for-the-badge">
</p>

English | [中文](#chinese)

</div>

---

# ✨ Overview

ResearchAgent is a lightweight Agent Framework designed for AI research.

Unlike frameworks such as LangChain or LangGraph, ResearchAgent is implemented completely from scratch to help developers understand the internal workflow of modern AI Agents.

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

# 简体中文

# 🔬 ResearchAgent

ResearchAgent 是一个**从零开始实现**的科研智能体（Research Agent）框架。

项目的目标不是封装复杂的 API，而是帮助开发者理解现代 Agent 的核心原理，并逐步构建一个可扩展的科研 Agent 平台。

---

## ✨ 项目特点

* 🧠 从零实现 ReAct Agent
* 🔧 插件化 Tool 系统
* 📦 Tool Registry
* 📄 PDF 阅读工具
* 🔍 论文搜索
* 📚 RAG（规划中）
* 🧠 Memory（规划中）
* 🤖 Multi-Agent（规划中）
* 💻 Code Agent（规划中）

---
## 🏛 系统架构

```text
用户
 │
 ▼
ResearchAgent
 │
 ▼
Tool Registry
 │
 ├── PDF Reader
 ├── Search
 ├── Python
 └── RAG
 │
 ▼
LLM
```

---

## 📌 开发路线

```text
v0.1
│
├── ReAct
├── Tool
├── Prompt
└── Agent Loop
↓
v0.2
Tool Registry
↓
v0.3
Prompt Builder
↓
v0.4
Action
↓
v0.5
Memory
↓
v0.6
Planner
↓
v0.7
Reflection
↓
v0.8
RAG
↓
v0.9
Multi-Agent
↓
v1.0
ResearchAgent Framework
```

---

## 🎯 项目目标

本项目不仅是一个 Agent Demo，更希望成为：

* Agent 学习框架
* Agent 科研实验平台
* RAG 实验平台
* 多智能体实验平台
* AI 论文研究工具

未来计划支持：

* 📄 自动阅读论文
* 🔍 自动搜索论文
* 💡 自动分析创新点
* 🧪 自动生成实验方案
* 💻 自动生成代码
* 📝 自动辅助论文写作

---

## ⭐ Star History

如果你觉得这个项目对你有所帮助，欢迎点一个 ⭐！
