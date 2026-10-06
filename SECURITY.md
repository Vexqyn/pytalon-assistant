# Security Policy

## Pytalon Assistant — Security Commitment

Pytalon Assistant is a **pure-Python, zero-dependency, console-based Assistant**.
It runs entirely on the learner's own computer, makes no network calls, and
stores only derived patterns and progress in local JSON files. Because of this
design, the attack surface is intentionally small — but security is still taken
seriously, and reports are always welcome.

This policy explains which versions receive security updates and how to report
a vulnerability responsibly.

---

## Supported Versions

Pytalon follows a **flagship-line support model**. Only the current flagship
line and the most recent hotfix line receive security updates.

| Version Line | Status                          | Security Updates |
| ------------ | ------------------------------- | ---------------- |
| 2.3.x        | Current flagship (Major Release)| :white_check_mark: |
| 2.2.x        | Previous stable line            | :x:              |
| 2.1.x        | Legacy hotfix line              | :x:              |
| 2.0.x        | Legacy stable line              | :x:              |
| < 2.0        | Historical previews             | :x:              |

**Notes**

- `2.3.x` is the only line actively maintained for security.
- Older lines are kept for learning and historical reference only.
- If a security issue is found in an unsupported line, the fix will be
  delivered in the current flagship line whenever technically possible.

---

## Reporting a Vulnerability

If you believe you have found a security vulnerability in Pytalon Assistant,
please report it **privately** so it can be investigated and fixed before any
public disclosure.

### Where to Report

Preferred channel:

- **GitHub Private Vulnerability Reporting**
  Open the repository, go to the **Security** tab, and use
  **"Report a vulnerability"**:
  `https://github.com/Vexqyn/pytalon-assistant/security/advisories/new`

Alternative channel (if private reporting is unavailable):

- Open a **minimal public issue** that only states *"I would like to report a
  security issue — please contact me privately."*
    
  - Do **not** include the technical details, proof-of-concept, or affected code
  in the public issue.

### What to Include in Your Report

To help reproduce and resolve the issue quickly, please include:

1. A clear description of the vulnerability.
2. The affected version (for example: `2.3`, `2.3.x`, or a specific commit).
3. The affected file(s) and function(s) if known.
4. Step-by-step reproduction instructions.
5. A minimal proof-of-concept, if one is safe to share privately.
6. The potential impact as you understand it.
7. Any suggested fix or mitigation (optional but appreciated).

Please **redact** any personal data, learner memory files, or machine-specific
paths before sharing logs or code snippets.

---

## What to Expect After Reporting

| Stage                        | Target Time             |
| ---------------------------- | ----------------------- |
| Initial acknowledgement      | Within 3 business days  |
| Triage and severity review   | Within 7 business days  |
| Status update to reporter    | Every 7 days while open |
| Fix or mitigation plan       | Within 30 days (when feasible) |
| Public disclosure (if any)   | After a fix is released |

**If the report is accepted**

- You will receive confirmation that the issue is valid.
- A fix will be prepared for the current flagship line (`2.3.x`).
- Credit will be given in the release notes unless you request anonymity.
- A coordinated disclosure date will be agreed with you before any public
  write-up.

**If the report is declined**

- You will receive a written explanation of why it was not treated as a
  security vulnerability.
- If it is better classified as a functional bug, it will be redirected to the
  normal issue tracker.
- You are still welcome to open a regular issue with the non-security details.

---

## Scope

**In scope**

- The Pytalon Assistant source code in this repository.
- Modules under `pytalon_body/` and `Pytalon_Memory/`.
- The practice executor in `utils.py`.
- The static database in `config.py`.
- Anything that could cause:

  - Unauthorized code execution during a practice session.
  - Escape from the practice sandbox.
  - Corruption or unintended deletion of `Pytalon_Memory/store/` files.
  - Leakage of data outside the learner's own machine.

**Out of scope**

- Vulnerabilities in Python itself or in the standard library.
- Issues in third-party tools used to clone or run the project.
- Social engineering against the learner or the developer.
- Denial-of-service by the learner against their own machine.
- Cosmetic issues, typos, or documentation clarity problems.
- Feature requests or general bug reports (use the issue tracker instead).

---

## Security Design Principles

Pytalon is built with the following guarantees in mind:

- **No network access** — the assistant never makes outbound calls.
- **No third-party dependencies** — only the Python standard library is used.
- **No raw utterance storage** — only derived patterns and progress are saved.
- **Atomic local writes** — memory files are written via a temporary file and
  an atomic replace, so a crash cannot leave a half-written file.
- **Sandboxed practice** — learner code runs under a restricted namespace with
  step limits, blocked `exit()` / `quit()`, and canned `input()` values.
- **Graceful degradation** — memory failures never crash a lesson.
- **No auto-deletion** — Pytalon never deletes learner memory on its own.

---

## Safe Harbor

Security research conducted in good faith against your **own local copy** of
Pytalon Assistant is welcome. You will not be pursued or reported for:

- Running the assistant locally.
- Fuzzing inputs against the validators or intent engine.
- Attempting to escape the practice sandbox on your own machine.
- Reporting findings privately through the channels above.

Please do **not**:

- Test against other learners' machines or memory stores.
- Publish exploit details before a fix has been released.
- Use findings to harm other users of the project.

---

## Thank You

Pytalon's philosophy is **"Honesty is the first feature."**  

- That applies to security too. If something feels unsafe, unclear, or unfair,
please say so — every serious report makes Pytalon stronger and more honest.

— **M. Qasim Farooqi (@acubura)**  
Creator of Pytalon Assistant
