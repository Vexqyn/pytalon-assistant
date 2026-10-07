# 🔐 Security Policy

## Pytalon Assistant — Security Commitment

Pytalon Assistant is a **pure-Python, zero-dependency, console-based assistant** designed to run entirely on the learner's own computer.

Pytalon makes **no network calls** and stores only derived patterns and learning progress in local JSON files. This intentionally keeps the attack surface small.

Security is still taken seriously, and responsible vulnerability reports are always welcome.

> **"Honesty is the first feature."**
>
> That principle applies to security too.

---

## 🛡️ Supported Versions

Pytalon follows a **flagship-line support model**. Only the current flagship
line receives active security maintenance.

| Version Line | Status | Security Updates |
| :--- | :--- | :---: |
| **2.3.x** | 🟢 Current flagship | ✅ |
| **2.2.x** | ⚪ Previous stable line | ❌ |
| **2.1.x** | ⚪ Legacy hotfix line | ❌ |
| **2.0.x** | ⚪ Legacy stable line | ❌ |
| **< 2.0** | ⚪ Historical previews | ❌ |

### Notes

- `2.3.x` is the **only actively maintained security line**.
- Older versions remain available for learning, experimentation, and historical reference.
- Security fixes for unsupported versions will generally be developed against the current `2.3.x` line.
- Users running unsupported versions are strongly encouraged to upgrade before reporting or relying on security fixes.

---

## 🚨 Reporting a Vulnerability

If you believe you have discovered a security vulnerability in Pytalon Assistant, please **report it privately**.

Private reporting gives the project an opportunity to investigate, reproduce, and fix the issue before technical details become public.

### 🔒 Preferred Channel — GitHub Private Vulnerability Reporting

Open the repository's **Security** tab and select **"Report a vulnerability"**:

`https://github.com/Vexqyn/pytalon-assistant/security/advisories/new`

This is the preferred method for reporting security-sensitive issues.

### 📝 Alternative Reporting Method

If GitHub Private Vulnerability Reporting is unavailable, open a **minimal public issue** containing only:

> I would like to report a security issue — please contact me privately.

**Do not include:**

- ❌ Exploit details
- ❌ Proof-of-concept code
- ❌ Sensitive logs
- ❌ Vulnerable source-code excerpts
- ❌ Personal or machine-specific information

The technical details should be shared privately after contact has been established.

---

## 📋 What to Include in Your Report

A useful security report should include as much of the following information as is safe to disclose privately:

1. **Vulnerability description**
   - What is wrong?
   - Why does it present a security risk?

2. **Affected version**
   - Example: `2.3`
   - Example: `2.3.x`
   - Or a specific commit hash.

3. **Affected components**
   - File(s)
   - Module(s)
   - Function(s)
   - Relevant configuration

4. **Reproduction steps**
   - Clear, minimal steps that reproduce the issue.

5. **Proof of concept**
   - Include a minimal PoC when it is safe and appropriate.

6. **Potential impact**
   - Explain what an attacker or malicious practice could potentially achieve.

7. **Suggested mitigation**
   - Optional, but highly appreciated.

### ⚠️ Please Redact Sensitive Information

Before sending logs, source code, or examples, remove:

- Personal information
- Learner memory contents
- Machine-specific paths
- Usernames
- Environment-specific secrets
- Other unrelated private data

---

## ⏱️ What to Expect After Reporting

We aim to handle security reports consistently and transparently.

| Stage | Target |
| :--- | :--- |
| 📩 Initial acknowledgement | Within **3 business days** |
| 🔎 Triage & severity review | Within **7 business days** |
| 🔄 Status updates | Every **7 days** while open |
| 🛠️ Fix or mitigation plan | Within **30 days**, when feasible |
| 📢 Public disclosure | After a fix is released |

These are **target response times**, not absolute guarantees. Complex vulnerabilities may require additional investigation or coordination.

---

## ✅ If the Report Is Accepted

When a report is confirmed as a security vulnerability:

- The issue will be investigated and tracked privately.
- A fix will be prepared for the current flagship line (`2.3.x`) where technically applicable.
- Affected users may be advised to upgrade.
- The reporter will receive updates during remediation.
- Security fixes may be accompanied by release notes or security advisories.
- Reporter credit will be provided where appropriate, unless anonymity is requested.
- A coordinated disclosure date may be agreed upon before public disclosure.

---

## ❌ If the Report Is Declined

If an issue is determined **not to be a security vulnerability**, the reporter will receive an explanation where appropriate.

Depending on the issue, it may instead be classified as:

- 🐛 A normal functional bug
- 💡 A feature request
- 📚 A documentation issue
- 🎨 A cosmetic issue
- ⚙️ An expected behavior

Security reports that are better suited to the normal issue tracker may be redirected there.

You are still welcome to submit a regular issue containing the appropriate non-security details.

---

# 🎯 Scope

## ✅ In Scope

The following areas are considered within the security scope:

- Pytalon Assistant source code in this repository.
- Modules under `pytalon_body/`.
- Modules under `Pytalon_Memory/`.
- The practice executor in `utils.py`.
- The static database in `config.py`.
- Local memory handling.
- Practice-session execution and isolation.

Security issues are especially relevant when they could result in:

- 🔴 Unauthorized code execution during a practice session.
- 🔴 Escape from the practice sandbox.
- 🔴 Unauthorized modification or corruption of learner memory.
- 🔴 Unintended deletion of files under `Pytalon_Memory/store/`.
- 🔴 Leakage of data outside the learner's intended local environment.
- 🔴 Circumvention of security controls implemented by Pytalon.

---

## ❌ Out of Scope

The following are generally outside the project's security scope:

- Vulnerabilities in Python itself.
- Vulnerabilities in the Python standard library.
- Security issues in third-party software used to clone, install, or execute Pytalon.
- Social engineering targeting learners or maintainers.
- Denial-of-service against the researcher's own machine.
- Cosmetic issues.
- Typos.
- Documentation clarity issues.
- Feature requests.
- General functional bugs without a security impact.

For these issues, please use the normal issue tracker instead.

---

# 🔐 Security Design Principles

Pytalon is designed around several security and privacy principles.

### 🌐 No Network Access

Pytalon is designed to operate locally and does not make outbound network calls.

### 📦 Zero Third-Party Dependencies

The project uses the **Python standard library only**, reducing dependency-related supply-chain risk.

### 🧠 No Raw Utterance Storage

Pytalon does not intentionally store raw learner utterances as permanent memory.

Only derived patterns and learning progress are persisted.

### 💾 Atomic Local Writes

Memory files are written through a temporary-file-and-replace process where applicable.

This helps prevent crashes or interruptions from leaving written memory files.

### 🧪 Sandboxed Practice

Learner practice code runs within a restricted execution environment designed to limit:

- Available functionality
- Execution time
- Process termination
- Interactive input

The practice environment blocks mechanisms such as `exit()` and `quit()` and provides canned `input()` values where required.

> ⚠️ **Important:** A Python-level sandbox should not be treated as equivalent to a hardened OS-level security boundary. Users should only execute untrusted practice code in environments appropriate for the level of isolation required.

### 🧯 Graceful Degradation

Memory or persistence failures should not unnecessarily crash an active lesson.

### 🗑️ No Automatic Memory Deletion

Pytalon does not intentionally delete learner memory as part of normal operation.

---

# 🤝 Safe Harbor

Security research conducted **in good faith against your own local copy of Pytalon Assistant** is welcome.

We encourage responsible research such as:

- 🧪 Running Pytalon locally.
- 🔍 Smart validators and intent-handling logic.
- 🧰 Testing malformed or unexpected inputs.
- 🧪 Attempting to escape the practice sandbox on your own machine.
- 📋 Reporting security findings privately.

### Researchers Should Not

Please do not:

- ❌ Test against other learners' machines.
- ❌ Access or modify other users' memory stores.
- ❌ Attempt to obtain data belonging to other users.
- ❌ Publish exploit details before reasonable remediation.
- ❌ Use discovered vulnerabilities to harm users.
- ❌ Conduct testing against infrastructure that you do not own or have explicit permission to test.

Safe harbor applies to **good-faith research conducted within these boundaries**.

---

# 📢 Coordinated Disclosure

When a vulnerability is confirmed, the project will make a reasonable effort to coordinate disclosure with the reporter.

Where practical:

1. 🔎 The vulnerability is privately investigated.
2. 🛠️ A fix or mitigation is developed.
3. 🧪 The fix is validated.
4. 📦 A patched release is published.
5. 📝 Relevant release notes or security documentation are updated.
6. 📢 Public disclosure occurs after remediation.

The exact timeline may vary depending on severity, complexity, affected versions, and the availability of a reliable fix.

---

# ❤️ Thank You

Security is a shared responsibility.

Pytalon's philosophy is:

> **"Honesty is the first feature."**

That applies to security too.

If something feels **unsafe, unclear, or unfair**, please report it. Every responsible security report helps make Pytalon stronger, safer, and more honest.

Thank you to everyone who takes the time to research, report, reproduce, and responsibly disclose security issues.

---

**— M. Qasim Farooqi (@acubura)**  
**Creator of Pytalon Assistant**

🔐 *Security reports are always appreciated. Thank you for helping keep Pytalon safe.*
