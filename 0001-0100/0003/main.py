from sympy import primefactors

FILENAME = "input.txt"


def get_input() -> int:
    with open(FILENAME) as file:
        return int(file.readline())


def main():
    num = get_input()
    result = primefactors(num)[-1]

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
