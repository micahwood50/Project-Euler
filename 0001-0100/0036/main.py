def main():
    result = 0

    for n in range(1, 1_000_000):
        s10 = str(n)
        s2 = bin(n)[2:]

        if s10 == s10[::-1] and s2 == s2[::-1]:
            result += n

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
