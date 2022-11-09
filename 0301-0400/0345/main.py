from itertools import permutations
from functools import lru_cache


FILENAME = "input.txt"


def get_input() -> list[list[int]]:
    matrix = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            matrix.append([int(n) for n in line.split()])

    return matrix


def get_max_matrix_sum(matrix: list[list[int]]) -> int:
    @lru_cache(None)
    def helper(remaining_col: tuple[int]) -> int:
        result = 0
        ri = 15 - len(remaining_col)
        for i, ci in enumerate(remaining_col):
            this_remaining_col = remaining_col[:i] + remaining_col[i + 1 :]
            result = max(result, matrix[ri][ci] + helper(this_remaining_col))

        return result

    return helper(tuple(range(len(matrix))))


def main():
    matrix = get_input()
    result = get_max_matrix_sum(matrix)

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
