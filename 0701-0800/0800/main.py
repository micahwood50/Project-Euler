from math import log
from sympy import sieve


def main():
    N = 800800
    upper_bound = N * log(N)
    primes_list = list(sieve.primerange(1, 20 * N))

    result = 0
    dj = 1

    for i in range(1, len(primes_list)):
        p = primes_list[i]
        q = primes_list[i - dj]

        while p * log(q) + q * log(p) > upper_bound and dj <= i:
            dj += 1
            q = primes_list[i - dj]

        result += i - dj + 1

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
