def main():
    result = 0
    modN = 10_000_000_000

    for n in range(1, 1_001):
        result += n**n
        result %= modN

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
