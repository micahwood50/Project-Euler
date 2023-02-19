from functools import lru_cache


def main():
    L = [200, 100, 50, 20, 10, 5, 2, 1]

    @lru_cache(None)
    def dp(n: int, coinIndex: int = 0) -> int:
        if n < 0 or coinIndex >= len(L):
            return 0

        if n == 0:
            return 1

        return dp(n - L[coinIndex], coinIndex) + dp(n, coinIndex + 1)

    print(f"Answer is {dp(200)}")


if __name__ == "__main__":
    main()
