MAX_INT = 10_000_000_000
UPPER_BOUND = 1_000_000_000
TARGET_NUM = 120


def bounded_pi(n: int, upper_bound: int) -> int:
    a, b = 1, 1
    result = 1

    while a != 0 or b != 1:
        if result > upper_bound:
            return -1

        a, b = b, (a+b)%n
        result += 1

    return result


def main():
    result = 0

    for n in range(TARGET_NUM, UPPER_BOUND):
        if bounded_pi(n, TARGET_NUM) == TARGET_NUM:
            result += n

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
