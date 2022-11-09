from sympy import divisors


def d(n: int) -> int:
    return sum(divisors(n)) - n


def is_abundant(n: int) -> bool:
    return d(n) > n


def main():
    abundant_set = set()
    S = set()

    for n in range(1, 28_123):
        for an in abundant_set:
            if n - an in abundant_set:
                break
        else:
            S.add(n)

        if is_abundant(n):
            abundant_set.add(n)

    print(f"Answer is {sum(S)}")


if __name__ == "__main__":
    main()
