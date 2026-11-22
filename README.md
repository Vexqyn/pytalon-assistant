<div align="center">
  <img src="https://github.com/user-attachments/assets/33dbbdea-f22b-418d-9640-ee57a74e88d1" alt="Pytalon Transparent Logo" width="250" style="margin-bottom: -10px;"/>
</div>

### A functional, customizable assistant engine, built in pure Python. The assistant is the core. Teaching is just one plugin.

https://github.com/user-attachments/assets/e763f3bc-22e7-48a0-90d4-ed6329cb65a6

<p align="center">
  <a href="https://github.com/Vexqyn/pytalon-assistant"><img src="https://img.shields.io/badge/Pytalon-2.3-brightgreen?style=for-the-badge" alt="Pytalon 2.3"></a>
  <img src="https://img.shields.io/badge/Python-pure%20Python-blue?style=for-the-badge" alt="Pure Python">
  <img src="https://img.shields.io/badge/Dependencies-none-success?style=for-the-badge" alt="No third-party dependencies">
  <img src="https://img.shields.io/badge/Interface-console-lightgrey?style=for-the-badge" alt="Console interface">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="MIT License"></a>
</p>

<p align="center">
  <a href="#-quick-start">🚀 Quick start</a> ·
  <a href="#-what-is-pytalon">✨ What is Pytalon?</a> ·
  <a href="#-how-the-current-application-works">🧭 How it works</a> ·
  <a href="CONTRIBUTING.md">🤝 Contributing</a>
</p>

---

> [!IMPORTANT]
> ## 🚧 Development update
> **This commit is not a new version of Pytalon.** The current code has a few known issues that I'm working on. This is a development push, and **Pytalon 2.3 remains the current version line.**

## ✨ What is Pytalon?

**Pytalon is not a tutor.**

It's a fully functional, customizable assistant, built like a plugin. The teaching part is just a plugin, not the core. Python teaching is simply the first thing built on top of it.

Pytalon is written in **pure Python with no external dependencies**. It runs on its own custom, fully functional pure-Python engine. No fuzzy-matching package is installed, and none is written. Everything, including the engine, is plain Python, and the whole system is customized like a plugin.

### 🔧 Where you can take it

Pytalon can be modified and adapted to any field you want:

- **Make it an LLM.** Do the LLM engineering, and it becomes an LLM model, in the same family as DeepSeek, Claude, ChatGPT, GLM, and others.
- **Put an AI model inside it.** Plug one in and Pytalon works with it.
- **Turn it into a Plugin House.** Pytalon uses all the plugins, MCP, tools, and connectors, and executes them too.
- **Make it a harness.** It becomes that as well.

In short: **the engine is the product, and the domain is yours to choose.** 🛠️

### 🧩 The idea in one glance

| Pytalon | In this project |
| --- | --- |
| **Core** | A customizable assistant engine |
| **Current plugin** | Python teaching, built on that engine |
| **Building blocks** | Conversation rules, configurable knowledge, behavior handling, and memory |
| **For engineers** | A pure-Python foundation to shape into your own assistant project |

### ⚙️ Built with Python, built to be customized

Pytalon uses only Python's standard library, so there are no third-party runtime dependencies. The engine is made from Python code, explicit rules, curated patterns, and configurable data. The only text-similarity helper is Python's built-in `difflib`.

The current implementation is local and console-based. Its modules and configuration are where you go to understand and reshape how the assistant behaves.

## 🌟 What Pytalon includes

| Feature | What it does |
| --- | --- |
| 🧠 **Rule-based conversation** | Detects configured intents such as greetings, requests, pauses, and clarifications |
| 🧰 **Custom response engine** | Uses curated language patterns, configurable rules, and Python-native matching |
| 🗂️ **Configurable knowledge** | Keeps phrases, patterns, behavior settings, and application data in Python modules |
| 💾 **Local memory** | Saves selected profile and progress data on your computer |
| 🎛️ **Behavior adaptation** | Uses derived counters to adjust some openings and prompts |
| 🧪 **Interactive practice runner** | Captures output, supplies canned input, and applies a line-step limit to submitted practice code |
| 🧱 **Modular structure** | Separates the app flow, assistant body, configuration data, and memory package |
| 📦 **No third-party packages** | Runs on Python's standard library alone |

## 🧩 Current plugin: Python teaching

The current app shows Pytalon in action through a conversational Python-learning experience. It greets you, responds to supported requests, guides the session, offers code practice, and gives you local progress summaries.

Teaching is **one plugin built with Pytalon**, not its whole identity. The lesson content lives in its own modules, so you can explore it, swap it, or replace it entirely.

## 🚀 Quick start

### Requirements

- **Python 3.15.2 or newer**
- A terminal or command prompt
- Nothing else. No packages to install.

### Download and run

```bash
git clone https://github.com/Vexqyn/pytalon-assistant.git
cd pytalon-assistant
python learning.py
```

If your system uses `python3`:

```bash
python3 learning.py
```

That's it. No environment setup and no `pip install`. 🐍

## 💬 See it in action

Start a session and talk to Pytalon in plain language:

```text
Pytalon, version 2.3, category: Major Release (Stable Version).

You: hi
Pytalon: Hey! Great to see you! Ready to learn some Python? Let's dive in!

You: (Type any response & Pytalon will talk to you)
```

The exact replies depend on the session path and your locally saved profile.

### 🗣️ Things to try

| Say or enter | What happens |
| --- | --- |
| `teach me variables` | Asks for a supported topic directly |
| `show topics` | Opens the topic menu |
| `not now` | Pauses at the current prompt |
| `what did you say?` | Recalls Pytalon's last response from this session |
| `what do you remember?` | Shows your locally saved profile and progress summary |
| `exit` | Ends the session |

## 🧭 How the current application works

```text
┌───────────────────────────────────────────────────────────────┐
│                    PYTALON SESSION FLOW                       │
├───────────────────────────────────────────────────────────────┤
│                                                               │
│  START                                                        │
│    │                                                          │
│    ├── Load local profile and progress                        │
│    ├── Open a conversation                                    │
│    ├── Detect a request using configured rules                │
│    ├── Route into the current teaching plugin                 │
│    ├── Offer an explanation, examples, or code practice       │
│    ├── Save selected progress locally                         │
│    └── Close with a session summary                           │
│                                                               │
│  Assistant engine → configurable behavior → plugin            │
└───────────────────────────────────────────────────────────────┘
```

## 🏗️ Architecture

Pytalon keeps its parts separate so each one can be understood and customized on its own.

| Part | Role |
| --- | --- |
| 🖥️ **Application** | Starts the session and coordinates the current experience |
| 🧠 **Assistant body** | Validates responses, detects intents, and derives behavior signals |
| ⚙️ **Configuration** | Exposes phrases, patterns, response data, and behavior thresholds |
| 💾 **Memory** | Tracks session context and saves selected profile and progress data |
| 🧩 **Plugin content** | Provides the current Python teaching experience |

### 📂 Project structure

```text
.
├── learning.py                  # Application entry point and session flow
├── intro.py                     # Opening conversation System & Topic selection as a plugin too
├── config.py                    # Configuration exports
├── utils.py                     # Custom Pure Python Engine & Helper Functions plus Practice Engine as a plugin too
├── validators.py                # Compatibility exports for assistant-body functions
├── topics_basic.py              # Teaching plugin content
├── topics_intermediate.py       # Teaching plugin content
├── pytalon_body/
│   ├── response_validators.py   # Response and prompt validation
│   ├── intent_engine.py         # Rule-based intent detection
│   └── behavior_learner.py      # Derived behavior signals and adaptation
├── static_database/
│   ├── response_phrases.py      # Yes, no, exit, and conversational response text
│   ├── conversation_patterns.py # Greeting, farewell, pause, and clarification patterns
│   ├── conversation_intents.py  # Conversation intent vocabulary
│   ├── topic_catalog.py         # Topic names and matching keywords
│   ├── topic_core.py            # Shared topic terms and command patterns
│   ├── topic_matching.py        # Topic matching rules and thresholds
│   ├── topic_patterns.py        # Combined topic and conversation pattern exports
│   ├── validator_sets.py        # Answer validation phrases and word sets
│   ├── behavior_settings.py     # Behavior markers and adaptation thresholds
│   ├── memory_patterns.py       # Memory request and response patterns
│   ├── practice_data.py         # Practice input responses
│   └── response_followups.py    # Follow-up response phrases
└── Pytalon_Memory/
    ├── conversation_context.py  # In-session context
    └── memory_store.py          # Local profile and progress storage
```

## 🔐 Local data and privacy

Pytalon's current application makes no network calls. Selected profile and progress data are stored as local JSON under `Pytalon_Memory/store/`, and Git ignores that folder.

The session context also has in-memory conversation-history methods. Session history and the saved profile/progress files are separate, so check the source and your local files to see what is held during a session and what is saved on your computer.

## 🛠️ Project status

Pytalon 2.3 is the current version line. The notice at the top describes the current development push: it is not a new release, and known issues are in development to be fixed.

## 🤝 Contributing

Want to help shape Pytalon? Contributions, issue reports, and clear feedback are all welcome! 🌱

- Read the [Contribution Guide](CONTRIBUTING.md) before opening a pull request.
- Follow the [Code of Conduct](CODE_OF_CONDUCT.md).
- For security concerns, follow the [Security Policy](SECURITY.md).
- For larger changes, open an issue first so we can talk through the direction.

The current runtime uses only the Python standard library. If you propose a third-party dependency, please explain why in your issue or pull request.

## 📜 License

Pytalon is released under the [MIT License](LICENSE). Please read the license file for its full terms and attribution requirements.

## ⭐ Support Pytalon

If Pytalon interests you, visit the [repository](https://github.com/Vexqyn/pytalon-assistant), explore the source, and share your feedback. Every thoughtful report helps the project grow. 💚

## 🎉 Pytalon Assistant Success Announcement

The original announcement celebrated Pytalon's community activity and shared these reported clone figures:

- 📈 **07/31–08/13:** 157 clones / 37 unique
- 📈 **08/13–08/26:** 477 clones / 60 unique
- 📈 **09/10–09/23:** 628 clones / 126 unique
- 📈 **09/15–09/28:** 661 clones / 129 unique

Pytalon 2.3 reached a reported peak of **543 clones in one day**, with reported totals of **1,923 clones** and **352 unique clones**.

Thank you to everyone who cloned, ran, and explored Pytalon. This is just the beginning! 😄

<p align="center">
  <img src="https://github.com/user-attachments/assets/97ae3cae-36b9-4dad-bf12-735f0e22a28d" alt="Pytalon Assistant success announcement and community clone statistics" width="100%">
</p>
