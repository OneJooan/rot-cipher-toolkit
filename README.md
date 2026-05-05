# ROT Cipher Toolkit

CLI tool for detecting, analyzing and decoding obfuscated text using classical ROT/Caesar cipher techniques and heuristic scoring.

---

## 🚀 Why this project exists

Simple obfuscation techniques are still commonly found in:

- CTF challenges
- Logs
- Malware samples
- Legacy scripts

This tool was built to:

- Understand how these techniques work
- Automate their analysis
- Simulate basic cryptanalysis workflows

---

## ✨ Features

- Encrypt / Decrypt files
- Brute-force ROT analysis
- Heuristic scoring system
- Top candidate detection
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

### JSON output

```bash
rot analiyze file.txt --json
```

## 🧠 How it works

The analysis mode evaluates all possible shifts (1–25) and ranks them based on:

- Common word detection
- Character validity ratio
- Letter frequency heuristics

## 🧪 Testing

```bash
pytest
```

## 📁 Structure

```bash
root_toolkit/
tests/
```

## ⚙️ Makefile Commands

Common development commands:

```bash
make install     # Install project
make test        # Run tests
make analyze FILE=example.txt
make encrypt FILE=file.txt SHIFT=13
```

## ⚠️ Disclaimer

This is not secure encryption.

This project is for:

- Education
- Cybersecurity practice
- Text analysis understanding