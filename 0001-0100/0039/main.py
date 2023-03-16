def main():
    result = 0
    p_result = 0

    for p in range(12, 1_000):
        solution_set = set()

        for a in range(p // 3):
            for b in range(a, 2 * p // 3):
                c = p - b - a

                if c <= b:
                    break

                if a**2 + b**2 == c**2:
                    solution_set.add((a, b, c))

        if result < len(solution_set):
            result = len(solution_set)
            p_result = p

    print(f"Answer is {p_result}")


if __name__ == "__main__":
    main()
