def recurring_length(n: int) -> int:
    i = 0
    r = 10
    seen = dict()

    while True:
        if r == 0:
            return 0

        if r in seen:
            return i - seen[r]

        seen[r] = i
        r = 10 * (r % n)
        i += 1


def main():
    result = max((recurring_length(i), i) for i in range(980, 985))[1]

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
