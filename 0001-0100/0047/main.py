from sympy import primefactors


def main():
    n = 647

    pfs = [len(primefactors(i)) for i in range(n, n + 4)]

    while True:
        if {*pfs} == {4}:
            print(f"Answer is {n}")
            return

        pfs = pfs[1:] + [len(primefactors(n + 4))]
        n += 1


if __name__ == "__main__":
    main()
