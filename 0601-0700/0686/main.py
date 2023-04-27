def main():
    result = 0
    num = 2
    count = 0

    while count < 678_910:
        if str(num)[:3] == "123":
            count += 1

        num <<= 1
        num = int(str(num)[:12])
        result += 1

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
