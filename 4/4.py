import pprint

def load_input():
    with open("4.data", "r") as data:
        matrix = []
        for index, line in enumerate(data):
            matrix.append(list())
            for letter in line.strip():
                matrix[index].append(letter)
        return matrix

def find_coordinates(matrix: list[list[chr]]) -> list[tuple[int, int]]:
    coordinates = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 'X':
                coordinates.append((row, col))

    return coordinates

def count_matches(matrix: list[list[chr]], coordinates: list[tuple[int, int]]) -> int:
    rows = len(matrix)
    cols = len(matrix[0])
    matches = 0
    # for each coordinate, explore all directions (ignore if x + 3 or y + 3 is out of bounds)
    for x, y in coordinates:
        # Horizontal
        if x + 3 < rows:
            if matrix[x + 1][y] == 'M' and matrix[x + 2][y] == 'A' and matrix[x + 3][y] == 'S':
                matches += 1
        if x - 3 >= 0:
            if matrix[x - 1][y] == 'M' and matrix[x - 2][y] == 'A' and matrix[x - 3][y] == 'S':
                matches += 1
        # Vertical
        if y + 3 < cols:
            if matrix[x][y + 1] == 'M' and matrix[x][y + 2] == 'A' and matrix[x][y + 3] == 'S':
                matches += 1
        if y - 3 >= 0:
            if matrix[x][y - 1] == 'M' and matrix[x][y - 2] == 'A' and matrix[x][y - 3] == 'S':
                matches += 1
        # Diagonal

        # Down+Right
        if x + 3 < rows and y + 3 < cols:
            if matrix[x + 1][y + 1] == 'M' and matrix[x + 2][y + 2] == 'A' and matrix[x + 3][y + 3] == 'S':
                matches += 1
        # Down+Left
        if x - 3 >= 0 and y + 3 < cols:
            if matrix[x - 1][y + 1] == 'M' and matrix[x - 2][y + 2] == 'A' and matrix[x - 3][y + 3] == 'S':
                matches += 1
        # Up+Right
        if x + 3 < rows and y - 3 >= 0:
            if matrix[x + 1][y - 1] == 'M' and matrix[x + 2][y - 2] == 'A' and matrix[x + 3][y - 3] == 'S':
                matches += 1
        # Up+Left
        if x - 3 >= 0 and y - 3 >= 0:
            if matrix[x - 1][y - 1] == 'M' and matrix[x - 2][y - 2] == 'A' and matrix[x - 3][y - 3] == 'S':
                matches += 1
    return matches


def main():
    data = load_input()
    # pprint.pp(data)
    # Find coordinates of all X's in matrix
    # Explore in both directions - horizontally, vertically, and diagonally for "XMAS"
    coordinates = find_coordinates(data)
    # print(coordinates)

    print(count_matches(data, coordinates))



if __name__ == '__main__':
    main()