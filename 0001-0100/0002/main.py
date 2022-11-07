FILENAME = "input.txt"


def get_input() -> int:
    with open(FILENAME) as file:
        input = int(file.readline())

    return input


def main():
    upper_limit = get_input()
    result = 0
    a, b = 1, 2

    while b <= upper_limit:
        result += b

        a, b = 2 * b + a, 3 * b + 2 * a

    print(f"The sum of the even-valued terms is {result}")


if __name__ == "__main__":
    main()
