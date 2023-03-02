from itertools import permutations


def main():
    for i, n in enumerate(permutations(range(10)), start=1):
        if i == 1_000_000:
            result = "".join(str(d) for d in n)
            print(f"Answer is {result}")
            break


if __name__ == "__main__":
    main()
