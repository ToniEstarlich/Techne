from pathlib import Path


def list_directory(path: str = ".") -> list[str]:
    """Return the files and directories inside a path."""
    directory = Path(path).expanduser().resolve()

    if not directory.exists():
        raise FileNotFoundError(f"Directory not found: {directory}")

    if not directory.is_dir():
        raise NotADirectoryError(f"Not a directory: {directory}")

    return [item.name for item in directory.iterdir()]


def read_file(path: str) -> str:
    """Read a UTF-8 text file."""
    file_path = Path(path).expanduser().resolve()

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if not file_path.is_file():
        raise IsADirectoryError(f"Not a file: {file_path}")

    return file_path.read_text(encoding="utf-8")