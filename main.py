#!/usr/bin/env python3
"""Write the entry sentence to /output/entry.txt."""

import os

SENTENCE = "Imagine every library, post office and town square in the world joined by wires, so any letter, book or spoken word reaches any door in the blink of an eye."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
