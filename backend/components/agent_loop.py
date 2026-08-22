import json

import ollama

from backend.components.agent_tools.tool_registry import get_tool, list_tools


def build_tools():
    """Build the tool definitions sent to Ollama."""
    tools = []

    for name in list_tools():
        tool = get_tool(name)

        parameters = {
            "type": "object",
            "properties": {},
            "required": [],
        }

        for parameter_name, parameter_type in tool["parameters"].items():
            parameters["properties"][parameter_name] = {
                "type": "string",
                "description": parameter_type,
            }

            if "optional" not in parameter_type:
                parameters["required"].append(parameter_name)

        tools.append(
            {
                "type": "function",
                "function": {
                    "name": name,
                    "description": tool["description"],
                    "parameters": parameters,
                },
            }
        )

    return tools


def run_agent(prompt: str, model: str = "llama3.2") -> str:
    """Send a request to Ollama and execute requested tools."""

    messages = [
        {
            "role": "user",
            "content": prompt,
        }
    ]

    response = ollama.chat(
        model=model,
        messages=messages,
        tools=build_tools(),
    )

    if not response.message.tool_calls:
        return response.message.content

    for call in response.message.tool_calls:
        tool_name = call.function.name
        arguments = call.function.arguments

        tool = get_tool(tool_name)

        if tool is None:
            return f"Unknown tool requested: {tool_name}"

        result = tool["function"](**arguments)

        messages.append(response.message)

        messages.append(
            {
                "role": "tool",
                "tool_name": tool_name,
                "content": json.dumps(result),
            }
        )

    final_response = ollama.chat(
        model=model,
        messages=messages,
    )

    return final_response.message.content