from pathlib import Path

from backend.config import MAX_REPAIR_ATTEMPTS
from backend.components.ask import ask_ollama
from backend.components.create_software import create_software
from backend.components.repair_project import repair_project
from backend.components.run_project import run_project
from backend.components.modify_project import modify_project

def build(user_idea: str) -> Path:
    """Generate, run and repair a software project."""

    print("Techne Builder is planning...")

    result = ask_ollama(user_idea)

    target = result.get("target", "PROJECT").upper()

    print(f"Target: {target}")
    print(f"Name: {result['project_name']}")
    print(f"Description: {result.get('description', '')}")

    software_dir = create_software(result)

    print(f"Created at: {software_dir}")

    # Internal tools are generated but not automatically executed.
    if target == "INTERNAL_TOOL":
        return software_dir

    for attempt in range(1, MAX_REPAIR_ATTEMPTS + 1):
        success, output = run_project(software_dir)

        if success:
            print("Project runs successfully.")
            return software_dir

        print(
            f"Project failed. "
            f"Repair attempt {attempt}/{MAX_REPAIR_ATTEMPTS}"
        )
        print(output)

        if attempt == MAX_REPAIR_ATTEMPTS:
            print("Maximum repair attempts reached.")
            return software_dir

        repaired = repair_project(software_dir, output)

        if not repaired:
            print("Unable to repair the project.")
            return software_dir

    return software_dir