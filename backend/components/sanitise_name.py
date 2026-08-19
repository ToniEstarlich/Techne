import re

def sanitise_name(name: str) -> str:
    """Convert a generated name into a safe directory or file name."""

    name = name.lower().strip()
    name = re.sub(r"[^a-z0-9_-]+", "-", name)
    name = re.sub(r"-+", "-", name)

    return name.strip("-") or "untitled"