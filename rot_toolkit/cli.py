#!/usr/bin/env python3

import argparse
import logging
import sys
import json
from pathlib import Path

from .core import rot_process
from .analysis import analyze_text

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")


def read_file(path):
    try:
        return Path(path).read_text(encoding="utf-8")
    except Exception as e:
        logging.error(f"Error reading file: {e}")
        sys.exit(1)


def read_stdin():
    if not sys.stdin.isatty():
        return sys.stdin.read()
    return None


def write_file(path, content):
    try:
        Path(path).write_text(content, encoding="utf-8")
    except Exception as e:
        logging.error(f"Error writing file: {e}")
        sys.exit(1)


def print_analysis(results, top=3, as_json=False):
    best = results[0]

    if as_json:
        output = {
            "best_shift": best[0],
            "score": best[2],
            "preview": best[1][:200],
            "alternatives": [
                {"shift": r[0], "score": r[2]} for r in results[:top]
            ]
        }
        print(json.dumps(output, indent=2))
        return

    confidence = "HIGH" if best[2] > 5 else "MEDIUM" if best[2] > 3 else "LOW"

    print("\n=== ANALYSIS RESULT ===\n")
    print(f"[+] Most probable shift: {best[0]}")
    print(f"[+] Confidence: {confidence}")
    print(f"[+] Score: {round(best[2], 2)}")

    print("\n--- Preview ---\n")
    print(best[1][:300])

    print("\n=== ALTERNATIVE RESULTS ===\n")
    for shift, text, score in results[:top]:
        print(f"[SHIFT {shift}] Score: {round(score,2)}")
        print(text[:150])
        print("-" * 40)


def main():
    parser = argparse.ArgumentParser(description="ROT Cipher Toolkit")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Encrypt
    enc = subparsers.add_parser("encrypt")
    enc.add_argument("file", nargs="?")
    enc.add_argument("--shift", type=int, required=True)
    enc.add_argument("--output", default="encrypted.txt")

    # Decrypt
    dec = subparsers.add_parser("decrypt")
    dec.add_argument("file", nargs="?")
    dec.add_argument("--shift", type=int, required=True)
    dec.add_argument("--output", default="decrypted.txt")

    # Analyze
    ana = subparsers.add_parser("analyze")
    ana.add_argument("file", nargs="?")
    ana.add_argument("--top", type=int, default=3)
    ana.add_argument("--json", action="store_true")

    args = parser.parse_args()

    content = read_stdin() or (read_file(args.file) if args.file else None)

    if not content:
        logging.error("No input provided")
        sys.exit(1)

    if args.command == "encrypt":
        result = rot_process(content, args.shift)
        write_file(args.output, result)
        logging.info(f"Encrypted → {args.output}")

    elif args.command == "decrypt":
        result = rot_process(content, -args.shift)
        write_file(args.output, result)
        logging.info(f"Decrypted → {args.output}")

    elif args.command == "analyze":
        results = analyze_text(content)
        print_analysis(results, args.top, args.json)


if __name__ == "__main__":
    main()