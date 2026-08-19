from backend.components.build import build


def main():
    idea = input("What do you want Techne to create?\n> ")

    if not idea.strip():
        raise SystemExit("No project idea provided.")

    build(idea)


if __name__ == "__main__":
    main()