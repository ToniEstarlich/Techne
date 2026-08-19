from pathlib import Path

from backend.components.ask import ask_ollama
from backend.components.read_project_files import read_project_files
from backend.components.write_files import write_files


def repair_project(project_dir: Path, error: str) -> bool:
    """Ask Ollama to analyse the error and repair the project."""

    print("Analysing error and preparing a repair...")

    project_files = read_project_files(project_dir)

    repair_prompt = f"""
The following Python project failed when executed.

PROJECT DIRECTORY:
{project_dir}

ERROR OUTPUT:
{error}

PROJECT FILES:
{project_files}

Analyse the error and repair the project.

Return only JSON using this structure:

{{
    "files": [
        {{
            "path": "relative/path/to/file.py",
            "content": "complete corrected file contents"
        }}
    ]
}}

Only include files that need to be changed.
"""

    result = ask_ollama(repair_prompt)

    files = result.get("files", [])

    if not files:
        print("The repair agent did not return any files.")
        return False

    write_files(project_dir, files)

    print(f"Repaired {len(files)} file(s).")

    return True