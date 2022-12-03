def main():
    result = 1
    n = 1

    for i in range(1, 501):
        for __ in range(4):
            n += 2 * i
            result += n

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
