from pathlib import Path

def read_project_files(project_dir: Path) -> str:
    """Read text-based project files for analysis by the repair agent."""

    files = []

    for path in project_dir.rglob("*"):
        if not path.is_file():
            continue

        # Ignore Python cache and Git files.
        if "__pycache__" in path.parts or ".git" in path.parts:
            continue

        try:
            content = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue

        relative_path = path.relative_to(project_dir)

        files.append(
            f"\n--- {relative_path} ---\n{content}"
        )

    return "\n".join(files)