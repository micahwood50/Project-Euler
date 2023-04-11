from math import gcd
from fractions import Fraction as F


def main():
    d_max = 1_000_000
    result = F(0, 1)
    target = F(3, 7)

    for d in range(1, d_max + 1):
        n = 3 * d // 7

        for dn in range(-2, 2):
            if gcd(n + dn, d) == 1 and result < F(n, d) < target:
                result = F(n, d)

    print(f"The answer is {result.numerator}")


if __name__ == "__main__":
    main()
