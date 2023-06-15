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
    factors = get_all_prime_number_below(7_376_508)  # generates 500,500 prime numbers
    modN = 500_500_507

    index = 0
    unoptimized_flag = True

    while unoptimized_flag:
        unoptimized_flag = False
        p = factors[index]
        optimal = p * p

        while optimal < factors[-1]:
            factors.pop()
            factors[index] *= optimal
            optimal *= optimal
            unoptimized_flag = True

        index += 1

    result = 1

    for factor in factors:
        result *= factor
        result %= modN

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
