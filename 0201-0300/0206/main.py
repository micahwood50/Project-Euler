def main():
    lower_bound = int(1_020_304_050_607_080_900 ** 0.5)
    upper_bound = int(1_929_394_959_697_989_990 ** 0.5) + 1

    n = lower_bound - lower_bound % 100 - 30

    while n <= upper_bound:
        if str(n*n)[::2] == "1234567890":
            print(f"Answer is {n}")
            return

        if n % 100 == 30:
            n += 40
        else:
            n += 60

    print("No answer!")

if __name__ == "__main__":
    main()
