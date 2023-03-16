from itertools import permutations


def is_prime(n: int) -> bool:
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def main():
    L = list(range(9, 0, -1))

    for i in range(9):
        for permutation in permutations(L[i:]):
            p_num = int("".join(map(str, permutation)))
            if is_prime(p_num):
                print(f"Answer is {p_num}")
                return

    print("No answer!")


if __name__ == "__main__":
    main()
