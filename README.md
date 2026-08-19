# Techne

**Techne is a local AI software-building agent designed to turn ideas into working software projects.**

Techne uses a local Ollama model to plan, generate, execute, and repair software projects.

The goal is simple:

> **Give Techne an idea. Get working software.**

## Current capabilities

Techne can currently:

* Generate Python software projects from natural-language descriptions.
* Create projects inside the `projects/` directory.
* Create internal Builder components.
* Generate structured project files using Ollama.
* Execute generated Python applications automatically.
* Provide test input to interactive applications.
* Detect execution errors.
* Ask Ollama to repair failed projects.
* Keep the Builder itself separated from generated user projects.
* Organize the Builder into reusable components.

## Architecture

```text
Techne/
│
├── backend/
│   ├── agent.py
│   ├── config.py
│   │
│   └── components/
│       ├── ask.py
│       ├── build.py
│       ├── create_software.py
│       ├── get_target.py
│       ├── modify_project.py
│       ├── read_project_files.py
│       ├── repair_project.py
│       ├── run_project.py
│       ├── sanitise_name.py
│       └── write_files.py
│
├── database/
├── frontend/
├── projects/
└── README.md
```

## How it works

A typical Techne workflow looks like this:

```text
User idea
    ↓
Techne
    ↓
Ollama
    ↓
Project plan
    ↓
File generation
    ↓
Project creation
    ↓
Automatic execution
    ↓
Error detection
    ↓
Repair
```

Techne is being developed incrementally. The architecture is intentionally modular so new capabilities can be added without turning the main agent into one large program.

## Requirements

* Python 3.10+
* Ollama
* A compatible local Ollama model

The current development configuration uses:

```text
llama3.2
```

## Running Techne

From the project root:

```powershell
python -m backend.agent
```

Then describe the software you want Techne to create.

For example:

```text
Create a simple Python calculator that asks for two numbers and displays their sum.
```

Generated projects are placed inside:

```text
projects/
```

## Development

Techne is currently an experimental project.

The focus is not only on generating code, but on eventually creating a complete software-development loop:

```text
Plan
  ↓
Build
  ↓
Run
  ↓
Test
  ↓
Repair
  ↓
Improve
  ↓
Repeat
```

Future capabilities may include:

* Better project modification
* Automated testing
* Code validation
* Project planning
* Specialized agents
* SEO agents
* Frontend generation
* Backend generation
* Database integration
* Multi-file debugging
* Better automated test generation
* Project quality evaluation

## Philosophy

Techne is being built around a simple idea:

**The quality of the final software matters more than the complexity of the agent that created it.**

The internal architecture will evolve as real projects expose new problems.

## Status

🚧 **Early development / experimental**

Techne is currently being tested through real generated projects and continuously improved based on the results.

## License

License information will be added as the project develops.
