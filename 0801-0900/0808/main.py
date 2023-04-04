from math import sqrt
from sympy import isprime


def prime_generator():
    yield 2
    n = 3

    while True:
        if isprime(n):
            yield n
        n += 2


def main():
    prime_gen = prime_generator()
    result = 0
    count = 0

    while count < 50:
        this_n = next(prime_gen) ** 2
        this_reversed_n = int(str(this_n)[::-1])

        if this_n != this_reversed_n:
            sqrt_reversed_n = round(sqrt(this_reversed_n))

            if sqrt_reversed_n**2 == this_reversed_n and isprime(sqrt_reversed_n):
                result += this_n
                count += 1

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
