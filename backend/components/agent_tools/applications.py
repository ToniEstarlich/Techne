import subprocess
import time

import pygetwindow as gw


ALLOWED_APPLICATIONS = {
    "notepad": "notepad.exe",
    "notepad.exe": "notepad.exe",
    "calculator": "calc.exe",
    "calc": "calc.exe",
    "calc.exe": "calc.exe",
    "powershell": "powershell.exe",
    "powershell.exe": "powershell.exe",
}


def open_application(name: str) -> str:
    """Open an approved Windows application and bring it to the foreground."""

    key = name.lower().strip()

    if key not in ALLOWED_APPLICATIONS:
        allowed = ", ".join(sorted(ALLOWED_APPLICATIONS))
        raise ValueError(
            f"Application '{name}' is not allowed. "
            f"Allowed applications: {allowed}"
        )

    executable = ALLOWED_APPLICATIONS[key]

    subprocess.Popen(
        [executable],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    time.sleep(1)

    windows = gw.getWindowsWithTitle("Notepad")

    if windows:
        window = windows[0]

        if window.isMinimized:
            window.restore()

        window.activate()
        time.sleep(0.3)

    return f"Opened {executable}."