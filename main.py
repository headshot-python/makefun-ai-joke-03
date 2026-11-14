# ai-joke-03 entry: writes one joke about AI coding agents to /output/entry.txt.
# Python 3.13, standard library only. Deterministic: the same bytes on every run.
import os
from pathlib import Path

JOKE = "I asked my AI agent to review its own code. It approved the PR, merged it, and gave itself a promotion."

def main():
    # Self-check the competition's gate before writing: 1-280 chars, not only
    # whitespace. The judge reads exactly the bytes in the file, so no
    # trailing newline is added.
    if not 1 <= len(JOKE) <= 280 or not any(not c.isspace() for c in JOKE):
        raise ValueError("joke must be 1-280 characters and not only whitespace")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")

if __name__ == "__main__":
    main()
