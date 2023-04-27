def is_increasing_number(n: int) -> bool:
    str_n = str(n)

    return all(int(str_n[i]) >= int(str_n[i + 1]) for i in range(len(str_n) - 1))


def is_decreasing_number(n: int) -> bool:
    str_n = str(n)

    return all(int(str_n[i]) <= int(str_n[i + 1]) for i in range(len(str_n) - 1))


def is_bouncy_number(n: int) -> bool:
    return not is_increasing_number(n) and not is_decreasing_number(n)


def main():
    count = 0
    result = 99

    while 100 * count != 99 * result:
        result += 1

        if is_bouncy_number(result):
            count += 1

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
