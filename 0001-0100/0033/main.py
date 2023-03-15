from fractions import Fraction as F


def main():
    num_result = 1
    den_result = 1

    for num in range(10, 99):
        for den in range(num + 1, 100):
            LS = len(set(str(num) + str(den)))
            if LS != 3 or num % 10 == den % 10 == 0:
                continue

            frac = F(num, den)

            try:
                if str(num)[1] == str(den)[0]:
                    sw_frac = F(int(str(num)[0]), int(str(den)[1]))

                else:
                    sw_frac = F(int(str(num)[1]), int(str(den)[0]))

                if sw_frac == frac:
                    num_result *= frac.numerator
                    den_result *= frac.denominator

            except ZeroDivisionError:
                continue

    result = F(num_result, den_result).denominator
    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
