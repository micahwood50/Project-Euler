from unittest import result


FILENAME = "input.txt"


def get_input() -> list[int]:
    num_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            num_list.append(int(line))

    return num_list


def main():
    num_list = get_input()

    result = str(sum(num_list))[:10]

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
