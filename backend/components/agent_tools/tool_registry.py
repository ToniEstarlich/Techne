from backend.components.agent_tools.filesystem import (
    list_directory,
    read_file,
)
from backend.components.agent_tools.terminal import run_command
from backend.components.agent_tools.applications import open_application


TOOLS = {
    "list_directory": {
        "description": "List files and directories inside a path.",
        "parameters": {
            "path": "string"
        },
        "function": list_directory,
    },
    "read_file": {
        "description": "Read the contents of a UTF-8 text file.",
        "parameters": {
            "path": "string"
        },
        "function": read_file,
    },
    "run_command": {
        "description": "Run a terminal command and return its result.",
        "parameters": {
            "command": "string",
            "cwd": "string, optional",
        },
        "function": run_command,
    },
    "open_application": {
        "description": "Open an approved Windows application.",
        "parameters": {
            "name": "string"
        },
        "function": open_application,
    },
}


def get_tool(name: str):
    """Return a registered tool definition."""
    return TOOLS.get(name)


def list_tools() -> list[str]:
    """Return the names of all registered tools."""
    return list(TOOLS.keys())