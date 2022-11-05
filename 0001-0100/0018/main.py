FILENAME = "input.txt"


def get_input() -> list[int]:
    int_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            int_list.append([int(n) for n in line.split()])

    return int_list


def get_max_path_sum(triangle_int: list[list[int]]) -> int:
    dp = dict()

    def helper(x: int, y: int) -> int:
        if (x, y) in dp:
            return dp[(x, y)]

        if y >= len(triangle_int):
            return 0

        dp[(x, y)] = triangle_int[y][x] + max(helper(x, y + 1), helper(x + 1, y + 1))

        return dp[(x, y)]

    return helper(0, 0)


def main():
    int_list = get_input()

    print(f"Answer is {get_max_path_sum(int_list)}")


if __name__ == "__main__":
    main()
