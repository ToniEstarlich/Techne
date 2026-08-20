from pathlib import Path

from backend.components.ask import ask_ollama
from backend.components.write_files import write_files


def build_web_app(
    project_dir: Path,
    user_idea: str,
) -> bool:
    """Generate a functional web application inside project_dir."""

    print("Techne Web App Builder is planning...")

    prompt = f"""
Create a complete, functional web application.

USER REQUIREMENT:
{user_idea}

TECHNOLOGY:
- Python backend
- Flask
- HTML
- CSS
- JavaScript only when necessary

REQUIREMENTS:
- The application must actually work.
- The backend entry point MUST be app.py.
- app.py must be located at the project root.
- The application must be runnable with:

    python app.py

- Use Flask.
- Use templates/ for HTML.
- Use static/ for CSS and JavaScript.
- Do not create nested duplicate project directories.
- Do not create placeholder files.
- Do not create empty files.
- Implement the requested functionality.
- Create a polished and responsive interface.
- Keep the architecture simple.

Return ONLY valid JSON:

{{
    "files": [
        {{
            "path": "app.py",
            "content": "complete file contents"
        }},
        {{
            "path": "templates/index.html",
            "content": "complete file contents"
        }},
        {{
            "path": "static/style.css",
            "content": "complete file contents"
        }}
    ]
}}

Only return files that are actually required.
"""

    result = ask_ollama(prompt)

    files = result.get("files", [])

    if not files:
        print("Web App Builder did not return any files.")
        return False

    write_files(project_dir, files)

    print(f"Generated web application with {len(files)} file(s).")

    return True