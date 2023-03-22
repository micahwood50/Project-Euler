from collections import Counter


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
    four_digit_prime_set = get_all_prime_number_below(
        10_000
    ) - get_all_prime_number_below(1_000)

    print("Possible answers: ")

    for p in four_digit_prime_set:
        for i in range(2, 3_334):
            p2 = p + i
            p3 = p2 + i
            if p2 in four_digit_prime_set and p3 in four_digit_prime_set:
                if Counter(str(p)) == Counter(str(p2)) == Counter(str(p3)):
                    print(f"    {p}{p2}{p3}")


if __name__ == "__main__":
    main()
