from math import acos, sqrt, pi
from itertools import combinations

FILENAME = "input.txt"


def get_input() -> list[tuple[tuple[int, int], tuple[int, int], tuple[int, int]]]:
    triangle_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            ax, ay, bx, by, cx, cy = list(map(int, line.strip().split(",")))
            triangle_list.append(((ax, ay), (bx, by), (cx, cy)))

    return triangle_list


def calculate_angle(p0: tuple[int, int], p1: tuple[int, int]) -> float:
    x0, y0 = p0
    x1, y1 = p1

    return acos(
        (x0 * x1 + y0 * y1) / (sqrt(x0**2 + y0**2) * sqrt(x1**2 + y1**2))
    )


def main():
    triangle_list = get_input()
    result = 0

    for points in triangle_list:
        sum_angles = 0

        for p0, p1 in combinations(points, 2):
            sum_angles += calculate_angle(p0, p1)

        if abs(sum_angles - 2 * pi) < 0.0000001:
            result += 1

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
