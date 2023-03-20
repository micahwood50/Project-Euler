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
    result = 9
    prime_set = get_all_prime_number_below(100_000)

    while True:
        if result in prime_set:
            result += 2
            continue

        for sq in range(1, int(((result - 3) // 2) ** 0.5) + 1):
            possiblyPrime = result - 2 * sq**2
            if possiblyPrime in prime_set:
                result += 2
                break
        else:
            print(f"Answer is {result}")
            return


if __name__ == "__main__":
    main()
