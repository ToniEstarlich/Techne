import subprocess


def run_command(command: str, cwd: str | None = None) -> dict:
    """Run a command and return its result."""

    result = subprocess.run(
        command,
        cwd=cwd,
        shell=True,
        capture_output=True,
        text=True,
        timeout=30,
    )

    return {
        "returncode": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
    }