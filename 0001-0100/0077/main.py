from functools import lru_cache
from sympy import primerange
from bisect import bisect


MAX_PRIME_BOUND = 200
PRIME_LIST = list(primerange(0, MAX_PRIME_BOUND))


def count_sum_primes(n: int) -> int:
    max_index = bisect(PRIME_LIST, n) - 1

    return _dp_count_sum_primes(n, max_index)


@lru_cache(None)
def _dp_count_sum_primes(n: int, index: int) -> int:
    if index < 0 or n < 0:
        return 0

    if index == 0:
        return 1 if n % 2 == 0 else 0

    if n == 0:
        return 1

    return _dp_count_sum_primes(n - PRIME_LIST[index], index) + _dp_count_sum_primes(
        n, index - 1
    )


def main():
    low_n = 10
    high_n = MAX_PRIME_BOUND
    count_target = 5_000

    while low_n < high_n:
        middle_n = (high_n + low_n) // 2
        count_result = count_sum_primes(middle_n)

        if count_result < count_target:
            low_n = middle_n + 1

        else:
            high_n = middle_n - 1

    print(f"Answer is {low_n}")


if __name__ == "__main__":
    main()
