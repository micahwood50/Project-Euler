def main():
    result = 1

    while (
        len(set(map(lambda n: frozenset(str(n)), (n * result for n in range(2, 7)))))
        > 1
    ):
        result += 1

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
