from collections import defaultdict, Counter


def main():
    result = 0
    cubes_dict = defaultdict(set)
    n = 1

    while True:
        cubed_n = n**3
        this_frozen_set = frozenset(Counter(str(cubed_n)).items())
        cubes_dict[this_frozen_set].add(cubed_n)

        if len(cubes_dict[this_frozen_set]) >= 5:
            result = min(cubes_dict[this_frozen_set])
            print(f"Answer is {result}")
            return

        n += 1


if __name__ == "__main__":
    main()
