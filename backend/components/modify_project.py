from pathlib import Path

from backend.components.ask import ask_ollama
from backend.components.read_project_files import read_project_files
from backend.components.write_files import write_files


def modify_project(project_dir: Path, user_request: str) -> bool:
    """Modify an existing project according to the user's request."""

    print("Analysing existing project...")

    project_files = read_project_files(project_dir)

    modify_prompt = f"""
You are modifying an existing software project.

PROJECT DIRECTORY:
{project_dir}

USER REQUEST:
{user_request}

CURRENT PROJECT FILES:
{project_files}

Modify the existing project according to the user's request.

Rules:
- Preserve the existing functionality unless the user asks to change it.
- Make the smallest changes necessary.
- Do not rewrite the project from scratch.
- Do not create unnecessary files.
- Do not create empty files.
- Do not create unused imports.
- Preserve the existing architecture where possible.
- Only include files that actually need to be changed.
- Return the complete contents of every changed file.

Return ONLY valid JSON using this structure:

{{
    "files": [
        {{
            "path": "relative/path/to/file.py",
            "content": "complete modified file contents"
        }}
    ]
}}
"""

    result = ask_ollama(modify_prompt)

    files = result.get("files", [])

    if not files:
        print("No files were modified.")
        return False

    write_files(project_dir, files)

    print(f"Modified {len(files)} file(s).")

    return True