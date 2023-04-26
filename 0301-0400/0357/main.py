from sympy import sieve, divisors


def main():
    N = 100_000_000
    result = 1

    primes_set = set(sieve.primerange(1, N + 2))

    for n in range(2, N + 1, 4):
        if n + 1 in primes_set and n // 2 + 2 in primes_set:
            this_divisors = divisors(n)[2:-1]

            for d in this_divisors:
                if d + n // d not in primes_set:
                    break

            else:
                result += n

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
