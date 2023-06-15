from itertools import accumulate

MOD_N = 1_000_000_007


def s(n):
    if n < 0:
        return 0

    if n < 10:
        return n

    if n // 9 > 10:
        return 9_999_999_999

    return int(str(n % 9) + "9" * (n // 9))


def S(k):
    return sum(s(n) for n in range(1, k + 1))


def f(n):
    if n < 0:
        return 0

    a, b = 0, 1

    for __ in range(n):
        a, b = b, a + b

    return a


def main():
    result = 0
    modN = 1_000_000_007

    print(f(90))

    sk = [s(n) for n in range(f(90))]

    Sk = list()
    acc = 0

    for sk_i in sk:
        acc = (acc + sk_i) % MOD_N
        Sk.append(acc)

    print(Sk[-4:])

    for i in range(2, 91):
        print(i)
        result += S(f(i))
        result %= modN

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
