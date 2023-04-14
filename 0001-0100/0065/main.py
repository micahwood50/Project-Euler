from fractions import Fraction as F


def main():
    result = 0
    seq = [2]

    for i in range(99):
        if i % 3 == 1:
            seq.append(2 * (i + 2) // 3)
        else:
            seq.append(1)

    convergent = seq.pop()

    for m in reversed(seq):
        convergent = m + F(1, convergent)

    for d in str(convergent.numerator):
        result += int(d)

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
