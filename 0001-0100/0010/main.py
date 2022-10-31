def get_primes(n):
    m = n + 1
    numbers = [True for __ in range(m)]
    for i in range(2, int(n**0.5 + 1)):
        if numbers[i]:
            for j in range(i*i, m, i):
                numbers[j] = False

    primes = list()
    for i in range(2, m):
        if numbers[i]:
            primes.append(i)

    return primes


def main():
    result = sum(get_primes(2_000_000))

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
