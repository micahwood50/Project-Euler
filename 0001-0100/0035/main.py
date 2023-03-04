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
    circular_primes_set = {2}

    for p in prime_set:
        if p in circular_primes_set:
            continue

        currStrPrime = str(p)

        for ch in currStrPrime:
            if ch in "02468":
                break
        else:
            currIntPrime = p
            this_set = set()

            for __ in str(p):
                if currIntPrime not in prime_set:
                    break

                this_set.add(currIntPrime)
                currStrPrime = currStrPrime[-1] + currStrPrime[:-1]
                currIntPrime = int(currStrPrime)

            else:
                circular_primes_set |= this_set

    print(f"Answer is {len(circular_primes_set)}")


if __name__ == "__main__":
    main()
