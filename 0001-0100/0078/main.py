from functools import lru_cache


def P(n: int) -> int:
    return (3 * n * n - n) // 2


@lru_cache(None)
def partitions(n):
    if n < 0:
        return 0

    if n < 2:
        return 1

    if n < 4:
        return n

    result = 0
    k = 1

    while (gi := P(k)) <= n:
        this_term = partitions(n - gi)
        result += -this_term if k % 2 == 0 else this_term
        k = -k if k > 0 else 1 - k

    return result


def main():
    result = 0
    while partitions(result) % 1_000_000 != 0:
        result += 1

    print(f"The answer is {result}")


if __name__ == "__main__":
    main()
