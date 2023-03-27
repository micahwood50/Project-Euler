def main():
    result = 0

    for a in range(2, 100):
        for b in range(2, 101):
            this_result = 0

            for d in str(a**b):
                this_result += int(d)

            result = max(result, this_result)

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
