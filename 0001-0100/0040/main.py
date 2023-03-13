def main():
    result = 1
    i = 1
    n = 1
    target_i = 1

    while i <= 1_000_000:
        str_n = str(n)
        for ii, d in enumerate(str_n, start=i):
            if ii == target_i:
                target_i *= 10
                result *= int(d)

        i += len(str_n)
        n += 1

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
