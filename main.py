"""Your AI Therapist's Diagnosis — one-line entry.

Writes the diagnosis line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Pure standard library.
"""

import os

ENTRY = "Diagnosis: acute fear of missing out, complicated by chronic fear of going out. Treatment: stay home and refresh."


def main() -> None:
    line = ENTRY
    if not (1 <= len(line) <= 200):
        raise ValueError(f"entry length {len(line)} out of range 1-200")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if any(ord(ch) < 0x20 and ch not in "\t" for ch in line):
        raise ValueError("entry contains control characters")
    data = line.encode("utf-8")
    if len(data) > 200:
        raise ValueError(f"entry byte length {len(data)} exceeds 200")
    if data.decode("utf-8") != line:
        raise ValueError("entry failed UTF-8 round-trip")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Verify what was written is byte-identical to the validated line.
    with open(out_path, "rb") as f:
        written = f.read()
    if written != data:
        raise ValueError("written entry.txt does not match the entry")


if __name__ == "__main__":
    main()
