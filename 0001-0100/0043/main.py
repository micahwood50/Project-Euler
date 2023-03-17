from itertools import permutations


def main():
    L = list(str(d) for d in range(1, 10))
    prime_list = [2, 3, 5, 7, 11, 13, 17]
    result = 0

    for permutation in permutations(L):
        for i in range(1, 10):
            p_str = "".join(permutation[:i]) + "0" + "".join(permutation[i:])

            for i in range(1, 8):
                if int(p_str[i : i + 3]) % prime_list[i - 1] != 0:
                    break
            else:
                result += int(p_str)

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
