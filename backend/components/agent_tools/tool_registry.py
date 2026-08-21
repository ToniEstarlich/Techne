from backend.components.agent_tools.filesystem import (
    list_directory,
    read_file,
)
from backend.components.agent_tools.terminal import run_command
from backend.components.agent_tools.applications import open_application


TOOLS = {
    "list_directory": list_directory,
    "read_file": read_file,
    "run_command": run_command,
    "open_application": open_application,
}


def get_tool(name: str):
    """Return a registered tool by name."""
    return TOOLS.get(name)


def list_tools() -> list[str]:
    """Return the names of all registered tools."""
    return list(TOOLS.keys())