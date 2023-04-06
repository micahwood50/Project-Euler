def square_digits(n: int) -> int:
    result = 0

    for ch in str(n):
        result += int(ch) ** 2

    return result


def main():
    set1 = {1}
    set89 = {89}

    for n in range(1, 10_000_000):
        this_set = set()

        while n not in set1 and n not in set89:
            this_set.add(n)
            n = square_digits(n)

        if n in set89:
            set89 |= this_set
        else:
            set1 |= this_set

    print(f"Answer is {len(set89)}")


if __name__ == "__main__":
    main()
