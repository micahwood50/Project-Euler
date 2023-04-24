def main():
    p = [16]
    current_p = 50

    while current_p <= 1_000_000_000:
        p.append(current_p)
        current_p = 4 * p[-1] - p[-2] + (12 if len(p) % 2 == 0 else -12)

    print(f"Answer is {sum(p)}")


if __name__ == "__main__":
    main()
