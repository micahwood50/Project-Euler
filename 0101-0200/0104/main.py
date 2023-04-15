def main():
    start_a, start_b = 1, 1
    end_a, end_b = 1, 1

    str_start_b = "1"
    str_end_b = "1"

    k = 2

    pandigital_target = set(str(d) for d in range(1, 10))

    while set(str_start_b) != pandigital_target or set(str_end_b) != pandigital_target:
        start_a, start_b = start_b, start_a + start_b
        end_a, end_b = end_b, end_a + end_b

        if len(str(start_b)) > 20:
            start_a = int(str(start_a)[:-1])
            start_b = int(str(start_b)[:-1])

        end_b %= 1_000_000_000

        str_start_b = str(start_b)[:9]
        str_end_b = str(end_b)

        k += 1

    print(f"Answer is {k}")


if __name__ == "__main__":
    main()
