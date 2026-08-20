# Techne

Techne is an experimental AI software-building agent.

The current goal is to make Techne capable of:

- understanding a software request
- planning a project
- generating project files
- running the generated application
- detecting errors
- repairing generated code
- iterating until the project works

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

## Current status

🚧 Work in progress.

Techne can currently generate simple Python projects and automatically
attempt to run and repair them.

The next stage is improving:

- web application generation
- project execution
- validation
- repair reliability
- frontend quality
- generated project architecture

The project is being developed incrementally while testing Techne
against real software projects.

## License

License information will be added as the project develops.
