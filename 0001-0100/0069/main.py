from sympy import totient


def main():
    result = 0
    max_value = 0

    for n in range(1, 1_000_000):
        this_value = n / totient(n)
        if this_value > max_value:
            max_value = this_value
            result = n

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
