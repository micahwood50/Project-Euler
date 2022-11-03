from functools import lru_cache


@lru_cache(None)
def get_collatz_chain_length(n: int) -> int:
    if n == 1:
        return 1

    return 1 + get_collatz_chain_length(n // 2 if n % 2 == 0 else 3 * n + 1)


def main():
    max_chain = 0
    result = 0

    for n in range(2, 1_000_000):
        this_chain = get_collatz_chain_length(n)
        if max_chain < this_chain:
            max_chain = this_chain
            result = n

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
