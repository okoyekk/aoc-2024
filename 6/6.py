from copy import deepcopy

import sys
import os

# Get the absolute path of the project root (folder A)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from debug import Debug  # noqa: E402
dbg = Debug(True)

direction_to_symbol = {0: '^', 1: '>', 2: 'v', 3: '<'}
symbol_to_direction = {'^': 0, '>': 1, 'v': 2, '<': 3}


def load_input():
    matrix = []
    with open("6.data", "r") as data:
        for line in data:
            matrix.append(list(line.strip()))

        return matrix


def get_guard_position(matrix: list[list[int]]) -> list[int]:
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] in symbol_to_direction:
                return [row, col]


def can_guard_exit(matrix: list[list[int]], guard_position: list[int]) -> bool:

    guard_row = guard_position[0]
    guard_col = guard_position[1]
    guard_symbol = matrix[guard_row][guard_col]

    rows = len(matrix)
    cols = len(matrix[0])

    if guard_symbol == '>':
        # '>' can exit on right edge (col = cols - 1)
        if guard_col == cols - 1:
            return True
    elif guard_symbol == '<':
        # '<' can exit on left edge (col = 0)
        if guard_col == 0:
            return True
    elif guard_symbol == '^':
        # '^' can exit on top edge (row = 0)
        if guard_row == 0:
            return True
    elif guard_symbol == 'v':
        # 'v' can exit on bottom edge (row = rows - 1)
        if guard_row == rows - 1:
            return True
    return False


def get_next_symbol(symbol: chr) -> chr:
    direction = symbol_to_direction[symbol]
    return direction_to_symbol[(direction + 1) % 4]


def move_guard_once(matrix: list[list[int]], guard_position: list[int]):
    # Doesn't verify if the new position isn't an obstacle
    guard_row = guard_position[0]
    guard_col = guard_position[1]
    guard_symbol = matrix[guard_row][guard_col]

    matrix[guard_row][guard_col] = 'X'  # Mark old position
    if guard_symbol == '>':
        matrix[guard_row][guard_col + 1] = guard_symbol
    elif guard_symbol == '<':
        matrix[guard_row][guard_col - 1] = guard_symbol
    elif guard_symbol == '^':
        matrix[guard_row - 1][guard_col] = guard_symbol
    elif guard_symbol == 'v':
        matrix[guard_row + 1][guard_col] = guard_symbol


def generate_guard_route(matrix: list[list[int]]) -> list[list[int]]:
    # 1. Get initial guard position and update it as matrix is mutated
    # 2. While guard cannot exit, move until the next obstacle (#) in direction
    #   a. Mark each visited cell with a X
    #   b. At obstacle, change direction and symbol
    guard_position = get_guard_position(matrix)

    while not can_guard_exit(matrix, guard_position):
        guard_symbol = matrix[guard_position[0]][guard_position[1]]

        rows = len(matrix)
        cols = len(matrix[0])

        if guard_symbol == '>':
            # '>' moves right (col + 1)
            while (guard_position[1] + 1 < cols) and (matrix[guard_position[0]][guard_position[1] + 1] != '#'):
                move_guard_once(matrix, guard_position)
                guard_position[1] += 1

            if (guard_position[1] + 1 < cols) and (matrix[guard_position[0]][guard_position[1] + 1] == '#'):
                matrix[guard_position[0]][guard_position[1]] = get_next_symbol(guard_symbol)
        elif guard_symbol == '<':
            # '<' moves left (col - 1)
            while (guard_position[1] - 1 >= 0) and (matrix[guard_position[0]][guard_position[1] - 1] != '#'):
                move_guard_once(matrix, guard_position)
                guard_position[1] -= 1

            if (guard_position[1] - 1 >= 0) and (matrix[guard_position[0]][guard_position[1] - 1] == '#'):
                matrix[guard_position[0]][guard_position[1]] = get_next_symbol(guard_symbol)
        elif guard_symbol == '^':
            # '^' moves up (row - 1)
            while (guard_position[0] - 1 >= 0) and (matrix[guard_position[0] - 1][guard_position[1]] != '#'):
                move_guard_once(matrix, guard_position)
                guard_position[0] -= 1

            if (guard_position[0] - 1 >= 0) and (matrix[guard_position[0] - 1][guard_position[1]] == '#'):
                matrix[guard_position[0]][guard_position[1]] = get_next_symbol(guard_symbol)
        elif guard_symbol == 'v':
            # 'v' moves down (row + 1)
            while (guard_position[0] + 1 < rows) and (matrix[guard_position[0] + 1][guard_position[1]] != '#'):
                move_guard_once(matrix, guard_position)
                guard_position[0] += 1

            if (guard_position[0] + 1 < rows) and (matrix[guard_position[0] + 1][guard_position[1]] == '#'):
                matrix[guard_position[0]][guard_position[1]] = get_next_symbol(guard_symbol)
    
    if can_guard_exit(matrix, guard_position):
        matrix[guard_position[0]][guard_position[1]] = 'X'
        return matrix


def count_occurences(matrix: list[list[int]], letter: chr) -> int:
    count = 0
    for row in matrix:
        for pos in row:
            if pos == letter:
                count += 1

    return count


def main():
    data = load_input()
    dbg.print("*****Input*****")
    dbg.pp(data)

    route = generate_guard_route(deepcopy(data))
    dbg.print("*****Route*****")
    dbg.pp(route)

    res = count_occurences(route, 'X')
    dbg.print(res)


if __name__ == '__main__':
    main()
