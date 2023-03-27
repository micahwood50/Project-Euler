def main():
    result = 0

    for a in range(1, 10):
        for b in range(50):
            if b == len(str(a**b)):
                result += 1

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
