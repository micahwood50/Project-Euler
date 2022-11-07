def difference(n: int) -> int:
    return (n * (n + 1) * (3 * n + 2) * (n - 1)) // 12


def main():
    result = difference(100)

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
