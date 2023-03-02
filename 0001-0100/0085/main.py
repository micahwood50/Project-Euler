def get_num_solutions(m: int, n: int) -> int:
    return m * (m + 1) * n * (n + 1) // 4


def main():
    minDiff = float("inf")
    result = (-1, -1)

    for m in range(2010):
        for n in range(2010):
            this_abs = abs(get_num_solutions(m, n) - 2_000_000)
            if this_abs < minDiff:
                result = (m, n)
                minDiff = this_abs

    w, h = result

    print(f"Answer is {w * h} (with grid {w} by {h})")


if __name__ == "__main__":
    main()
