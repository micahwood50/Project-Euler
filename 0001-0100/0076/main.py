from functools import lru_cache


def dp(target: int) -> int:
    return dp_helper(target, target - 1)


@lru_cache(None)
def dp_helper(target: int, max_value: int) -> int:
    if target < 0:
        return 0

    if target <= 1:
        return 1

    if max_value == 1:
        return 1

    return sum(dp_helper(target - n, n) for n in range(1, max_value + 1))


def main():
    print(f"Answer is {dp(100)}")


if __name__ == "__main__":
    main()
