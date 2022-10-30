from itertools import product


def isPythagoreanTriplet(a: int, b: int, c: int) -> bool:
    return a**2 + b**2 == c**2


def main():
    for a in range(1, 499):
        for b in range(a + 1, 999):
            c = 1_000 - a - b

            if c <= b:
                continue

            if isPythagoreanTriplet(a, b, c):
                print(f"The product abc is {a*b*c}")


if __name__ == "__main__":
    main()
