FILENAME = "input.txt"


def get_matrix() -> list[list[int]]:
    matrix = list()

    with open(FILENAME) as file:
        for line_row in file.readlines():
            matrix.append(list(map(int, line_row.strip().split(","))))

    return matrix


def main():
    matrix = get_matrix()
    dp_matrix = [[-1 for __ in row] for row in matrix]
    dp_matrix[0][0] = matrix[0][0]

    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if i == 0 and j == 0:
                continue

            up_val, left_val = float("inf"), float("inf")

            if i != 0:
                up_val = dp_matrix[i - 1][j]

            if j != 0:
                left_val = dp_matrix[i][j - 1]

            dp_matrix[i][j] = min(up_val, left_val) + col

    print(f"Answer is {dp_matrix[-1][-1]}")


if __name__ == "__main__":
    main()
