from itertools import permutations as P


def main():
    L = [str(i) for i in range(1, 10)]
    set_product = set()
    result = 0

    for p in P(L):
        for i in range(1, 8):
            for j in range(i + 1, 9):
                n1 = int("".join(p[:i]))
                n2 = int("".join(p[i:j]))
                n3 = int("".join(p[j:]))

                if n1 * n2 == n3:
                    if n3 not in set_product:
                        set_product.add(n3)
                        result += n3

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
