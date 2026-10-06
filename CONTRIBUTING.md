# 🤝 Contributing to Pytalon

> *"Honesty is the first feature. Intelligence is the second. Everything else is polish."*
> — **Pytalon 2.3 Philosophy**

Thank you for wanting to make **Pytalon** better! Contributions are welcome — you don't have to be an expert to help. Whether you fix a typo, improve a lesson, or report a bug, you're making Python easier for every learner who comes after you.

Please read this guide before opening an issue or pull request. It keeps the project honest, stable, and easy to maintain.

---

## 📋 Table of Contents

- [📜 Code of Conduct](#-code-of-conduct)
- [🧠 Ways to Contribute](#-ways-to-contribute)
- [🚀 Getting Started](#-getting-started)
- [🏗️ Project Structure](#️-project-structure)
- [✏️ Coding Conventions](#️-coding-conventions)
- [🐛 Reporting Bugs](#-reporting-bugs)
- [💡 Suggesting Features](#-suggesting-features)
- [🔀 Pull Request Process](#-pull-request-process)
- [✅ Pull Request Checklist](#-pull-request-checklist)
- [📜 License](#-license)

---

## 📜 Code of Conduct

By participating in this project, you agree to be kind, respectful, and honest. Feedback is welcome; hostility is not. See the [Code of Conduct](CODE_OF_CONDUCT.md) for details.

---

## 🧠 Ways to Contribute

| Type | What it looks like |
|------|--------------------|
| 🧠 **Lessons** | Improve beginner-friendly explanations in `topics_basic.py` / `topics_intermediate.py`. |
| ✏️ **Clarity** | Fix grammar, typos, or confusing wording anywhere in the code or docs. |
| ➕ **New Content** | Add new beginner topics or advanced modules (see [Coding Conventions](#️-coding-conventions)). |
| 🧪 **Practice** | Add more practice exercises with clear instructions and expected keywords. |
| 🐛 **Bug Fixes** | Squash bugs — especially the ones that should have died in 2.3. |
| 💡 **Features** | Suggest or build new learning, validation, or memory features. |
| 🗣️ **Feedback** | Give honest feedback on Pytalon as a flagship Non-AI model. |

> 💛 **Remember:** Finding and reporting a bug isn't complaining — it's contributing.

---

## 🚀 Getting Started

### 1️⃣ Fork and clone the repository

```bash
git clone https://github.com/<your-username>/pytalon-assistant.git
cd pytalon-assistant
```

### 2️⃣ Verify your environment

- **Python 3.14.8 or higher** (`python --version`)
- **No external libraries needed** — Pytalon is 100% Python Standard Library.

> 🟢 **Zero dependencies is a feature, not an accident.** Please don't add third-party packages (see [Coding Conventions](#️-coding-conventions)).

### 3️⃣ Run the program

```bash
python learning.py
```

**For Linux/macOS users:** If `python` doesn't work, use `python3 learning.py` instead.

### 4️⃣ Create a branch

```bash
git checkout -b fix/short-description
# or
git checkout -b feature/short-description
```

Use a clear branch name, e.g. `fix/negation-detection`, `feature/loops-topic`, `docs/readme-typo`.

---

## 🏗️ Project Structure

Know where your change belongs before you start:

| Path | Responsibility |
|------|----------------|
| `learning.py` | Entry point — session loop and topic dispatch. |
| `intro.py` | Introduction and session setup. |
| `topics_basic.py` | Teaching functions for basic topics (1–6). |
| `topics_intermediate.py` | Intermediate topics (7–13). |
| `config.py` | **Single static knowledge base** — responses, phrases, topics, thresholds. |
| `validators.py` | Thin compatibility layer over `pytalon_body/`. |
| `utils.py` | Shared utilities (menus, practice, custom matching). |
| `pytalon_body/` | Real body: `response_validators.py`, `intent_engine.py`, `behavior_learner.py`. |
| `Pytalon_Memory/` | Persistent memory: `memory_store.py` (JSON on disk), `conversation_context.py` (RAM only). |
| `Pytalon_Memory/store/` | **Learner data — gitignored. Never commit this.** |
| `.github/` | Issue templates and CI workflows. |

**Single-responsibility rule of thumb:** App teaches · body understands · memory persists · config knows. Put new code in the layer that owns that job.

---

## ✏️ Coding Conventions

Follow the existing style — the 2.3 overhaul happened precisely to make the code readable.

1. **🐍 Standard library only.** No third-party dependencies. Allowed modules: `difflib`, `re`, `io`, `sys`, `json`, `os`, `datetime`, and other stdlib essentials.
2. **📄 Module docstrings.** Every file starts with a `# filename.py` comment and a docstring stating its purpose (see existing files).
3. **🎯 Single responsibility.** Split giant functions; give each layer a clear job. No god-functions.
4. **⚡ Lazy, intentional imports.** Import submodules where needed — eager imports slow `learning.py` startup (see `pytalon_body/__init__.py`).
5. **🛡️ Graceful degradation.** Wrap optional systems (especially memory) in `try/except` so a failure never crashes a lesson.
6. **🗣️ Honest, natural language.** New phrases belong in `config.py`, written the way people actually talk — no robotic patterns.
7. **🔍 Inspectable logic only.** Pytalon is a rule-based, threshold-based Non-AI model. Never add LLM/cloud calls; when unsure, the code should **ask**, not guess.
8. **🔒 Privacy first.** Never commit learner personal data or `Pytalon_Memory/store/` contents. Behavior learning stores derived counters — never raw messages.
9. **🚫 No secrets.** Don't commit API keys, tokens, or credentials — CI runs Bandit and dependency reviews on every PR.

---

## 🐛 Reporting Bugs

1. Search [existing issues](https://github.com/Vexqyn/pytalon-assistant/issues) first — duplicates slow everyone down.
2. Open a new issue using the **[🐛 Bug Report](https://github.com/Vexqyn/pytalon-assistant/issues/new?template=🐛-bug-report.md)** template.
3. Include:
   - **Steps to reproduce** (exact input you typed)
   - **Expected vs. actual behavior**
   - **Python version** and **OS**
   - Screenshot or error text, if any

---

## 💡 Suggesting Features

1. Use the **[✨ Feature Request](https://github.com/Vexqyn/pytalon-assistant/issues/new?template=✨-feature-request.md)** template.
2. Explain the **learning problem** it solves, not just the feature itself.
3. Small, focused suggestions are easier to act on than big vague ones.

---

## 🔀 Pull Request Process

1. **Open an issue first** for anything beyond small fixes — let's agree on the direction before code.
2. **Branch from `main`:**

   ```bash
   git checkout main
   git pull
   git checkout -b fix/short-description
   ```

3. **Make focused commits.** One concern per PR. Commit messages should be short and descriptive, e.g.:

   ```text
   Fix negation handling in yes/no validator
   Add practice exercise for loops topic
   Clarify explanation of f-strings in topic 9
   ```

4. **Test manually before pushing:**

   ```bash
   python learning.py
   ```

   Walk through the affected topic, try edge-case inputs (empty input, negations like "no not really", slang like "lock in"), and confirm nothing crashes — including memory failures.

5. **Push and open a PR:**

   ```bash
   git push origin fix/short-description
   ```

   Then open a Pull Request against `main` with a clear title and description (what changed and why).

6. **CI must pass.** Every PR runs automated checks:

   | Workflow | What it checks |
   |----------|----------------|
   | **Bandit** | Python security issues. |
   | **Security Scanning** | Broader security analysis. |
   | **Dependency Review** | Blocks GPL/LGPL-licensed dependencies and risky dependency changes. |
   | **Scorecard** | Supply-chain security best practices. |

7. **Respond to review.** Maintainers may ask for changes — that's part of keeping Pytalon honest and stable.

---

## ✅ Pull Request Checklist

Before you request review, confirm:

- [ ] Branch is up to date with `main`
- [ ] `python learning.py` runs without errors
- [ ] The affected topic(s) and practice(s) were tested manually
- [ ] Code follows the conventions above (stdlib only, docstrings, single responsibility)
- [ ] No learner data from `Pytalon_Memory/store/` is committed
- [ ] New phrases/word-sets live in `config.py`, not scattered across files
- [ ] Commit messages are short and descriptive
- [ ] The PR description explains **what** changed and **why**
- [ ] Linked issue (if any) is referenced, e.g. `Fixes #12`

---

## 📜 License

By contributing, you agree that your contributions will be licensed under the **[MIT License](https://github.com/Vexqyn/pytalon-assistant/blob/main/LICENSE)** that covers this project.

---

> 🐍 **Happy Coding, and thank you for helping Pytalon stay honest!**
> — M. Qasim Farooqi (@acubura)
