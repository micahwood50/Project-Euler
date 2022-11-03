FILENAME = "input.txt"


def get_input() -> list[list[int]]:
    matrix = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            matrix.append(list(map(int, line.split())))

    return matrix


def main():
    matrix = get_input()
    N = 4
    result = 0

    directions = [
        [(i, 0) for i in range(N)],
        [(0, i) for i in range(N)],
        [(i, i) for i in range(N)],
        [(N - i - 1, i) for i in range(N)],
    ]

    for i in range(len(matrix) - N + 1):
        for j in range(len(matrix[0]) - N + 1):
            for d in directions:
                try:
                    this_product = 1
                    for dx, dy in d:
                        x = j + dx
                        y = i + dy

                        this_product *= matrix[y][x]

                        result = max(result, this_product)

                except IndexError:
                    continue

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
