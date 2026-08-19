from pathlib import Path

from backend.components.get_target import get_target_directory
from backend.components.sanitise_name import sanitise_name
from backend.components.write_files import write_files


def create_software(result: dict) -> Path:
    """Create generated software in its appropriate location."""

    target = result.get("target", "PROJECT").upper()
    base_dir = get_target_directory(target)

    name = sanitise_name(result["project_name"])
    software_dir = base_dir / name

    software_dir.mkdir(parents=True, exist_ok=True)

    write_files(software_dir, result.get("files", []))

    return software_dir