from math import comb


def main():
    result = 0

    for n in range(1, 101):
        for r in range(3, n - 1):
            if comb(n, r) > 1_000_000:
                result += 1

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
