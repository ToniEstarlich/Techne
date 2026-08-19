from pathlib import Path

from backend.config import INTERNAL_TOOLS_DIR, PROJECTS_DIR


def get_target_directory(target: str) -> Path:
    """Return the correct directory for generated software."""

    if target == "INTERNAL_TOOL":
        return INTERNAL_TOOLS_DIR

    if target == "PROJECT":
        return PROJECTS_DIR

    raise ValueError(f"Unknown target: {target}")