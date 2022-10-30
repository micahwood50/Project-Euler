FILENAME = "input.txt"


def get_input() -> str:
    num_str = ""

    with open(FILENAME) as file:
        for line in file.readlines():
            num_str += line.strip()

    return "".join(num_str)


def main():
    num_str = get_input()
    result = 0
    N = 13

    for i in range(len(num_str) - N):
        this_result = 1
        for d in num_str[i : i + N]:
            this_result *= int(d)

        result = max(result, this_result)

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
