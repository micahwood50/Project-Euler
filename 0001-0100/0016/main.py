def main():
    n = 2**1_000
    result = 0

    for d in str(n):
        result += int(d)

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
