from math import sqrt
from itertools import combinations


def small_power_set_generator(s):
    n = len(s)
    for r in range(1, n // 2 + 2):
        for combo in combinations(s, r):
            yield combo


def T(N: int) -> int:
    result = 0

    for n in range(9, int(sqrt(N)) + 1):
        if n % 9 > 1:
            continue

        sq_n = n**2
        str_sq_n = str(sq_n)

        for p in small_power_set_generator(range(1, len(str(sq_n)))):
            this_str_sq_n = str_sq_n
            for i in p[::-1]:
                this_str_sq_n = this_str_sq_n[:i] + "+" + this_str_sq_n[i:]
            try:
                if n == eval(this_str_sq_n):
                    result += sq_n
                    break
            except SyntaxError:
                continue

    return result


def main():
    N = 1_000_000_000_000

    print(f"Answer is {T(N)}")


if __name__ == "__main__":
    main()
