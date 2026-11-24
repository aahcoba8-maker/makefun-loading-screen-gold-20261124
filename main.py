"""Loading-screen tip for stressed developers and AI coding agents.

Writes one line (<=200 chars) to entry.txt in MAKEFUN_OUTPUT_DIR,
falling back to the script directory when the variable is unset.
Stdlib only.
"""

import os

TIP = (
    "TIP: Red build? Commit what passes, let the agent rerun the "
    "failing test, and take a walk. Ten minutes away fixes more bugs "
    "than two hours staring at red."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    os.makedirs(out_dir, exist_ok=True)
    text = TIP.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
