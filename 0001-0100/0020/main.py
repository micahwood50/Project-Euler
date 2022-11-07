def main():
    result = 0
    N = 1

    for i in range(2, 101):
        N *= i

    for d in str(N):
        result += int(d)

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
