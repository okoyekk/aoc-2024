import sys
import os

# Get the absolute path of the project root (folder A)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from debug import Debug  # noqa: E402
dbg = Debug(True)


def load_input():
    matrix = []
    with open("sample.data", "r") as data:
        for line in data:
            matrix.append(list(line.strip()))

        return matrix


def main():
    data = load_input()
    dbg.pp(data)


if __name__ == '__main__':
    main()
