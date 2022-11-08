from math import factorial


def factorial_digits(n: int) -> int:
    return sum(factorial(int(ch)) for ch in str(n))


def main():
    result = 0

    en = 1
    while 10**en - 1 <= en*factorial(9):
        en += 1

    for n in range(3, 10**en):
        if n == factorial_digits(n):
            result += n

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
