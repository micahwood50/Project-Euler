def main():
    N = 28433 * 2**7830457 + 1
    modN = 10_000_000_000

    print(f"Answer is {N % modN}")


if __name__ == "__main__":
    main()
