from pathlib import Path

def write_files(base_dir: Path, files: list) -> None:
    """Write generated files while preventing path traversal."""

    for file in files:
        relative_path = Path(file["path"])

        file_path = (base_dir / relative_path).resolve()

        if base_dir.resolve() not in file_path.parents:
            raise ValueError(f"Unsafe file path: {file['path']}")

        file_path.parent.mkdir(parents=True, exist_ok=True)

        file_path.write_text(
            file["content"],
            encoding="utf-8",
        )