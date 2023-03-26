def is_palindrome(n: int) -> bool:
    str_n = str(n)

    return str_n == str_n[::-1]


def rev_num(n: int) -> int:
    return int(str(n)[::-1])


def main():
    result = 0

    for n0 in range(10_000):
        n = n0
        for __ in range(50):
            n += rev_num(n)
            if is_palindrome(n):
                break
        else:
            result += 1

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
