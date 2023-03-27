from fractions import Fraction


def main():
    term = Fraction(1, 1)
    result = 0

    for __ in range(1_001):
        term = 1 + Fraction(1, 1 + term)
        if len(str(term.numerator)) > len(str(term.denominator)):
            result += 1

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
