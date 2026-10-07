# 🤝 Contributing to Pytalon

> *"Honesty is the first feature. Intelligence is the second. Everything else is polish."*
> — **Pytalon 2.3 Philosophy**

Contributions are welcome — you don't have to be an expert to help. A typo fix, a clearer explanation, a bug report: every change makes Pytalon better for the learner who comes next.

This guide explains how to report issues, propose changes, and get your pull request merged. Please read it before opening an issue or PR.

**TL;DR:** Fork → branch → change → `python learning.py` → open a PR.

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

By participating in this project, you agree to be kind, respectful, and honest. Feedback is welcome; hostility is not. The full [Code of Conduct](CODE_OF_CONDUCT.md) applies to every project space.

---

## 🧠 Ways to Contribute

| Type | What it looks like |
|------|--------------------|
| **Lessons** | Improve beginner-friendly explanations in `topics_basic.py` / `topics_intermediate.py`. |
| **Clarity** | Fix grammar, typos, or confusing wording anywhere in the code or docs. |
| **New content** | Add a new beginner topic or advanced module (see [Coding Conventions](#️-coding-conventions)). |
| **Practice** | Add exercises with clear instructions and expected keywords. |
| **Bug fixes** | Squash bugs — especially the ones that should have died in 2.3. |
| **Features** | Suggest or build new learning, validation, or memory features. |
| **Feedback** | Honest thoughts on Pytalon as a flagship Non-AI model. |

> Finding and reporting a bug isn't complaining — it's contributing.

For anything beyond a small fix, [open an issue first](#-suggesting-features) so we can agree on the direction before code is written.

---

## 🚀 Getting Started

### Prerequisites

| Requirement | Details |
|-------------|---------|
| **Python** | 3.14.8 or newer — check with `python --version` |
| **Libraries** | None. Pytalon is 100% Python Standard Library. |
| **Tools** | Git |

Zero dependencies is a feature, not an accident — please don't add third-party packages.

### Step 1 — Fork and clone

```bash
git clone https://github.com/<your-username>/pytalon-assistant.git
cd pytalon-assistant
```

### Step 2 — Create a branch

```bash
git checkout -b fix/short-description      # bug fixes
git checkout -b feature/short-description  # new ideas
git checkout -b docs/short-description     # documentation only
```

Pick a short, specific name — for example `fix/negation-detection`, `feature/loops-topic`, or `docs/readme-typo`.

### Step 3 — Run the program

```bash
python learning.py
```

On Linux/macOS, use `python3 learning.py` if `python` doesn't work. You're ready to make changes.

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

**Rule of thumb:** App teaches · body understands · memory persists · config knows. Put new code in the layer that owns that job.

---

## ✏️ Coding Conventions

The 2.3 overhaul exists to keep this code readable — please keep it that way.

| Convention | What it means |
|------------|---------------|
| **Standard library only** | No third-party dependencies. Allowed: `difflib`, `re`, `io`, `sys`, `json`, `os`, `datetime`, and other stdlib essentials. |
| **Module docstrings** | Every file starts with a `# filename.py` comment and a docstring stating its purpose. |
| **Single responsibility** | Split giant functions; give each layer one clear job. No god-functions. |
| **Lazy, intentional imports** | Import submodules where needed — eager imports slow `learning.py` startup (see `pytalon_body/__init__.py`). |
| **Graceful degradation** | Wrap optional systems (especially memory) in `try/except` so a failure never crashes a lesson. |
| **Honest, natural language** | New phrases belong in `config.py`, written the way people actually talk — no robotic patterns. |
| **Inspectable logic only** | Pytalon is rule-based and threshold-based — never add LLM/cloud calls. When unsure, the code should ask, not guess. |
| **Privacy first** | Never commit learner data or `Pytalon_Memory/store/`. Behavior learning stores derived counters — never raw messages. |
| **No secrets** | No API keys, tokens, or credentials — CI runs Bandit and dependency review on every PR. |

---

## 🐛 Reporting Bugs

1. Search [existing issues](https://github.com/Vexqyn/pytalon-assistant/issues) first — duplicates slow everyone down.
2. Open a new issue with the **[🐛 Bug Report](https://github.com/Vexqyn/pytalon-assistant/issues/new?template=🐛-bug-report.md)** template.
3. Include:

   - **Steps to reproduce** — the exact input you typed
   - **Expected vs. actual behavior**
   - **Python version** and **OS**
   - Screenshot or error text, if any

---

## 💡 Suggesting Features

1. Use the **[✨ Feature Request](https://github.com/Vexqyn/pytalon-assistant/issues/new?template=✨-feature-request.md)** template.
2. Explain the **learning problem** it solves, not just the feature itself.
3. Keep suggestions small and focused — they're easier to act on than big vague ones.

---

## 🔀 Pull Request Process

1. **Open an issue first** for anything beyond small fixes — let's agree on the direction before code.

2. **Branch from `main`:**

   ```bash
   git checkout main
   git pull
   git checkout -b fix/short-description
   ```

3. **Make focused commits.** One concern per PR. Keep commit messages short and descriptive:

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

5. **Push and open a PR** against `main` with a clear title and description (what changed and why):

   ```bash
   git push origin fix/short-description
   ```

6. **Make sure CI passes.** Every PR runs these automated checks:

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

Thank you for helping Pytalon stay honest — and happy coding.

— M. Qasim Farooqi (@acubura)
