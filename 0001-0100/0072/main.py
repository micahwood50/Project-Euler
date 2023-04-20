from sympy.ntheory.factor_ import totient


def main():
    result = 0

    for d in range(2, 1_000_001):
        result += totient(d)

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
