import ctypes
import time

import pyautogui
import pygetwindow as gw


def focus_window(title: str) -> str:
    """Find a window by title and force it to the foreground."""

    windows = gw.getWindowsWithTitle(title)

    if not windows:
        raise RuntimeError(f"Window '{title}' was not found.")

    window = windows[0]

    if window.isMinimized:
        window.restore()

    hwnd = window._hWnd

    ctypes.windll.user32.ShowWindow(hwnd, 9)
    ctypes.windll.user32.SetForegroundWindow(hwnd)

    time.sleep(0.5)

    return f"Focused window: {window.title}"


def type_text(text: str) -> str:
    """Type text into the currently focused application."""

    pyautogui.write(text, interval=0.03)

    return f"Typed: {text}"