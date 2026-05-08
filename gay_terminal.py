#!/usr/bin/env python3
import sys

RESET = "\033[0m"
BOLD = "\033[1m"
COLORS = [
    "\033[31m",
    "\033[33m",
    "\033[32m",
    "\033[36m",
    "\033[34m",
    "\033[35m",
]

lines = [
    "hello from the gay terminal",
    "love is loud",
    "pride, chaos, and a little sparkle",
]

for i, line in enumerate(lines):
    color = COLORS[i % len(COLORS)]
    print(f"{color}{BOLD}{line}{RESET}")

print()
print("".join(f"{c}█{RESET}" for c in COLORS))
print()
print("✨ stay fabulous ✨")
