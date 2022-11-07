from sympy import divisors


def d(n: int) -> int:
    return sum(divisors(n)) - n


def main():
    S = set()

    for n in range(1, 10_001):
        if n in S:
            continue

        dn = d(n)
        if n != dn and d(dn) == n:
            S.add(n)
            S.add(dn)

    print(f"Answer is {sum(S)}")


if __name__ == "__main__":
    main()
