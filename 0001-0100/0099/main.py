from math import log

FILENAME = "input.txt"


def get_input() -> list[tuple[int, int]]:
    result = []

    with open(FILENAME) as file:
        for line in file.readlines():
            result.append(list(map(int, line.split(","))))

    return result


def main():
    base_exp = get_input()
    result = 0
    max_value = 0

    for i, (base, exp) in enumerate(base_exp, start=1):
        calculated_result = exp * log(base)

        if calculated_result > max_value:
            max_value = calculated_result
            result = i

    print(f"The answer is {result}")


if __name__ == "__main__":
    main()
