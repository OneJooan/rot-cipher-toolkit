# ROT Cipher Toolkit

Lightweight cryptanalysis CLI tool for detecting and decoding simple text obfuscation techniques such as ROT/Caesar ciphers.

---

## 🚀 Why this project exists

Simple obfuscation techniques are still commonly found in:

- CTF challenges
- Logs
- Malware samples
- Legacy scripts

Despite their simplicity, these techniques are still used to hide information in multiple contexts.

The goal of this tool is to:

- Understand how these techniques work
- Automate their analysis
- Simulate basic cryptanalysis workflows

---

## 📦 Installation

Clone the repository and install in editable mode:

```bash
git clone <repo-url>
cd rot-cipher-toolkit
pip install -e .
```

---

## ✨ Features

- File encryption and decryption (ROT-based)
- Brute-force ROT analysis (1–25 shifts)
- Heuristic-based scoring system
- Automatic best candidate detection
- JSON output for automation
- stdin support (pipeline ready)

---

## 🧰 Usage

### Encrypt

```bash
rot encrypt file.txt --shift 13
```

### Decrypt

```bash
rot decrypt file.txt --shift 13
```

### Analyze

```bash
rot analyze file.txt
```

### Analyze (JSON output)

```bash
rot analyze file.txt --json
```

### Pipeline

```bash
cat file.txt | rot analyze
```

#### Example
```text
[INFO] Most probable shift: 13
[INFO] Confidence: HIGH

Hello world, this is a test message
```

#### Example use case

Analyzing obfuscated input from logs or suspicious sources:

```text
Input:
Gur synt vf va gur ebbz

Output:
The flag is in the room
```

---

## 🧠 How it works

The analysis mode evaluates all possible shifts (1–25) and ranks them based on:

- Common word detection
- Character validity ratio
- Letter frequency analysis

---

## 🧪 Testing

Run tests with:

```bash
pytest
```

---

## 📁 Structure

```text
.
├── rot_toolkit/
├── tests/
├── README.md
├── Makefile
└── pyproject.toml
```

---

## ⚙️ Makefile Commands

Common development commands:

```bash
make install     # Install project
make test        # Run tests
make analyze FILE=example.txt
make encrypt FILE=file.txt SHIFT=13
make decrypt FILE=file.txt SHIFT=13
```

## ⚠️ Disclaimer

This is not secure encryption.

Do not use this tool for protecting sensitive data.

This project is for:

- Education
- Cybersecurity practice
- Text analysis understanding
