from sympy import sieve


def main():
    max_num = 50_000_000
    prime_list = list(sieve.primerange(7100))
    n_set = set()

    for p1 in prime_list:
        for p2 in prime_list:
            for p3 in prime_list:
                this_n = p1**2 + p2**3 + p3**4
                if this_n < max_num:
                    n_set.add(this_n)
                else:
                    break

    print(f"Answer is {len(n_set)}")


if __name__ == "__main__":
    main()
