from sympy import isprime


def generator_spiral():
    n = 1
    dx = 2
    while True:
        for __ in range(4):
            n += dx
            yield n
        dx += 2


def main():
    prime_count = 0
    total_count = 1
    ratio = 1

    gen = generator_spiral()

    while ratio >= 0.1:
        for __ in range(4):
            if isprime(next(gen)):
                prime_count += 1

        total_count += 4
        ratio = prime_count / total_count

    result = -next(gen) + next(gen) - 1

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
