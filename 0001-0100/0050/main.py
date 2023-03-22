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
    prime_set = get_all_prime_number_below(1_000_000)
    prime_list = sorted(prime_set)
    acc_sum_primes = []
    p_sum = 0
    i = 0

    while p_sum < 1_000_000:
        p_sum += prime_list[i]
        i += 1
        acc_sum_primes.append(p_sum)

    max_length = 0
    result = 0

    for i in range(len(acc_sum_primes) - 1):
        for j in range(i + 1, len(acc_sum_primes)):
            n = acc_sum_primes[j] - acc_sum_primes[i]

            if n in prime_set:
                if max_length < j - i:
                    max_length = j - i
                    result = n

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
