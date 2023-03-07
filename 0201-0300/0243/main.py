from sympy.ntheory.factor_ import totient


def get_all_prime_number_below(n: int) -> list[int]:
    sieve = [True for __ in range(n + 1)]
    prime_list = [2]

    for i in range(3, n, 2):
        if sieve[i]:
            prime_list.append(i)

        for j in range(i, n + 1, i):
            sieve[j] = False

    return prime_list


def main():
    prime_list = get_all_prime_number_below(1_000)
    i = 1
    d = 1

    while i < len(prime_list):
        for __ in range(4):
            d *= 2

            if 94744 * totient(d) < 15499 * (d - 1):
                break

        else:
            d //= 16
            d *= prime_list[i]
            i += 1
            continue

        break

    print(f"Answer is {d}")


if __name__ == "__main__":
    main()
