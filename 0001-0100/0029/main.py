def main():
    num_set = set()

    for a in range(2, 101):
        for b in range(2, 101):
            num_set.add(a**b)

    print(f"Answer is {len(num_set)}")


if __name__ == "__main__":
    main()
