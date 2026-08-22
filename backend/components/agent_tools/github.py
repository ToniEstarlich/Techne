import subprocess


def _run_git(args):
    """Run a Git command from the Techne project root."""
    result = subprocess.run(
        ["git", *args],
        capture_output=True,
        text=True,
        cwd=".",
    )

    return {
        "returncode": result.returncode,
        "stdout": result.stdout.strip(),
        "stderr": result.stderr.strip(),
    }


def git_status():
    """Return the current Git status of Techne."""
    return _run_git(["status", "--short", "--branch"])


def git_add(files=None):
    """Stage files for the next commit."""
    if files is None:
        files = ["."]

    if isinstance(files, str):
        files = [files]

    return _run_git(["add", *files])


def git_commit(message):
    """Create a Git commit with the supplied message."""
    if not message or not message.strip():
        raise ValueError("Commit message cannot be empty.")

    return _run_git(["commit", "-m", message])


def git_push():
    """Push the current branch to its configured remote."""
    return _run_git(["push"])