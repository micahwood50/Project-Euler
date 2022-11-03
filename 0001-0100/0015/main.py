from math import comb


def main():
    N = 20
    result = comb(2 * N, N)

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
