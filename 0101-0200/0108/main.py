def main():
    n = 0
    distinct_solutions = 0

    while distinct_solutions < 1_000:
        n += 1260
        distinct_solutions = 0

        for y in range(n + 1, 2 * n + 1):
            x = y * n // (y - n)

            if n * (x + y) == x * y:
                distinct_solutions += 1

    print(f"Answer is {n}")


if __name__ == "__main__":
    main()
