from pathlib import Path
import re
import subprocess
import sys


def generate_test_input(source: str) -> str:
    """Generate simple test input based on input() usage."""

    inputs = re.findall(
        r"(?:int|float)\s*\(\s*input\s*\([^)]*\)\s*\)",
        source,
    )

    generic_inputs = re.findall(
        r"input\s*\([^)]*\)",
        source,
    )

    total_inputs = max(len(inputs), len(generic_inputs))

    if total_inputs == 0:
        return ""

    test_values = []

    for index in range(total_inputs):
        if index < len(inputs):
            test_values.append("10")
        else:
            test_values.append("Valencia")

    return "\n".join(test_values) + "\n"


def run_project(project_dir: Path) -> tuple[bool, str]:
    """Run the project's main Python entry point with generated test input."""

    main_file = project_dir / "main.py"

    if not main_file.exists():
        return False, "No main.py file was found in the project."

    print("Running project...")

    source = main_file.read_text(encoding="utf-8")

    test_input = generate_test_input(source)

    try:
        result = subprocess.run(
            [sys.executable, str(main_file)],
            cwd=project_dir,
            input=test_input,
            capture_output=True,
            text=True,
            timeout=15,
        )

    except subprocess.TimeoutExpired:
        return False, "The project exceeded the 15 second execution timeout."

    output = ""

    if result.stdout:
        output += f"STDOUT:\n{result.stdout}\n"

    if result.stderr:
        output += f"STDERR:\n{result.stderr}\n"

    if result.returncode == 0:
        return True, output

    return False, output