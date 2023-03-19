def P(n: int) -> int:
    return n * (3 * n - 1) // 2


def main():
    L = [1, 5]
    S = set(P(n) for n in range(10_000))
    n = 3

    while True:
        L.append(P(n))
        n += 1

        for i in range(len(L) - 2, 0, -1):
            sumP = L[-1] + L[i]
            diffP = L[-1] - L[i]

            if sumP in S and diffP in S:
                print(f"Answer is {diffP}")
                return


if __name__ == "__main__":
    main()
