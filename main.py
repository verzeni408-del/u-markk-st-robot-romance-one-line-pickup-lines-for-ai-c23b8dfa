"""Robot Romance: one-line pickup line for an AI.

Writes a single pickup line to /output/entry.txt.
"""

import os

LINE = "I told the AI I loved it, and it updated its privacy policy to include my feelings."
OUT_PATH = "/output/entry.txt"


def main():
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "line must be 1-200 characters"
    assert "\n" not in text, "line must be a single line"
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
