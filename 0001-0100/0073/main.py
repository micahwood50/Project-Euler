from math import gcd


def main():
    result = 0

    for d in range(4, 12_001):
        for n in range(d // 3 + 1, (d + 1) // 2):
            if gcd(n, d) == 1:
                result += 1

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
