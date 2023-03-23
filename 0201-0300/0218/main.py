from itertools import product


def main():
    result = 0

    factors = [2, 3, 7]

    for p, u, v in product(factors, repeat=3):
        a = u**2 - v**2
        b = 2 * u * v
        s = a * b * (a**2 - b**2)

        if s % p:
            result += 1

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
