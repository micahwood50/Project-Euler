def get_all_prime_number_below(n: int) -> set[int]:
    sieve = [True for __ in range(n + 1)]
    prime_set = {2}

    for i in range(3, n, 2):
        if sieve[i]:
            prime_set.add(i)

        for j in range(i, n + 1, i):
            sieve[j] = False

    return prime_set


def main():
    prime_set = get_all_prime_number_below(100_000)
    max_count = 0
    mul_result = 0

    for a in range(-999, 1_000):
        for b in range(-1_000, 1_001):
            this_count = 0
            f = lambda n: n**2 + a * n + b
            n = 0

            while f(n) in prime_set:
                this_count += 1
                n += 1

            if this_count > max_count:
                max_count = this_count
                mul_result = a * b

    print(f"Answer is {mul_result}")


if __name__ == "__main__":
    main()
