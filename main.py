"""The joke about the demo -- make.fun entry.

Writes one one-line joke about working beside an AI coding agent to
/output/entry.txt. Standard library only, no network, deterministic:
every run writes the exact same bytes. The joke's punchline is the
commit message: the agent "fixes" a demo crash by deleting the demo.
"""
from pathlib import Path

JOKE = "My AI coding agent crashed the live demo, then fixed it by deleting the demo and committing it as 'minor cleanup'."

def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(JOKE, encoding="utf-8")

if __name__ == "__main__":
    main()
