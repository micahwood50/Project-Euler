FILENAME = "input.txt"


def get_input() -> list[str]:
    str_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            str_list.extend(line.strip().split('","'))

    str_list[0] = str_list[0][1:]
    str_list[-1] = str_list[-1][:-1]

    return str_list


def get_name_score(name: str) -> int:
    name = name.lower()
    result = 0

    for ch in name:
        result += ord(ch) - ord("a") + 1

    return result


def main():
    name_list = get_input()
    name_list.sort()

    result = 0

    for i, name in enumerate(name_list, start=1):
        result += i * get_name_score(name)

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
