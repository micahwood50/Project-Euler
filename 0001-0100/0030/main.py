def main():
    result = 0
    fifth_power_map = {str(i): i**5 for i in range(10)}

    for n in range(10, 1_000_000):
        s = 0
        for d in str(n):
            s += fifth_power_map[d]

        if n == s:
            result += n

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
