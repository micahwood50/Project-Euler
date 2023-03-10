from itertools import permutations as P


def main():
    L = list(str(n) for n in range(1, 10))
    result = 0

    for length in range(1, 5):
        for p in P(L, length):
            i = 1
            S = set()
            str_n = "".join(p)
            n = int(str_n)
            this_n = n
            set_n = set(p)

            while not (S & set_n) and "0" not in S:
                S |= set_n
                i += 1
                this_n = i * n
                set_n = set(str(this_n))

            if len(S) == 9 and "0" not in S:
                this_result = ""

                for ii in range(1, i):
                    this_result += str(ii * n)

                result = max(result, int(this_result))

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
