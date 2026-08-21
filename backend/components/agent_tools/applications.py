import subprocess


ALLOWED_APPLICATIONS = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "powershell": "powershell.exe",
}


def open_application(name: str) -> str:
    """Open an approved Windows application."""

    key = name.lower().strip()

    if key not in ALLOWED_APPLICATIONS:
        allowed = ", ".join(sorted(ALLOWED_APPLICATIONS))
        raise ValueError(
            f"Application '{name}' is not allowed. "
            f"Allowed applications: {allowed}"
        )

    subprocess.Popen(
        [ALLOWED_APPLICATIONS[key]],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    return f"Opened {key}."