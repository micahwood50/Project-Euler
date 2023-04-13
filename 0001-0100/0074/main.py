from math import factorial


def digit_factorial(n: int) -> int:
    result = 0

    for d in str(n):
        result += factorial(int(d))

    return result


def main():
    result = 0

    for n in range(1, 1_000_000):
        seen_set = set()

        while n not in seen_set:
            seen_set.add(n)
            n = digit_factorial(n)

        if len(seen_set) == 60:
            result += 1

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
