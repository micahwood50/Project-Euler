from sympy import totient
from collections import Counter


def main():
    min_ratio = 100
    result = 0

    for n in range(2, 10_000_000):
        this_totient = totient(n)

        if Counter(str(n)) == Counter(str(this_totient)):
            this_ratio = n / this_totient
            if this_ratio < min_ratio:
                result = n
                min_ratio = this_ratio

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
