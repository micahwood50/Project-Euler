def nth_prime_number(n):
    prime_list = [2]
    num = 3

    while len(prime_list) < n:

        for p in prime_list:
            if num % p == 0:
                break
        else:
            prime_list.append(num)

        num += 2

    return prime_list[-1]


def main():
    result = nth_prime_number(10_001)

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
