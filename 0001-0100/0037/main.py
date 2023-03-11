from functools import lru_cache
from itertools import product


@lru_cache(None)
def is_prime(n: int) -> bool:
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def is_truncatable_prime(str_n: str) -> bool:
    if len(str_n) <= 1:
        return False

    if not is_prime(int(str_n)):
        return False

    for i in range(1, len(str_n)):
        s1 = str_n[:i]
        s2 = str_n[i:]

        if not is_prime(int(s1)) or not is_prime(int(s2)):
            return False

    return True


def main():
    result = 0
    truncatable_prime_set = set()
    num_repeat = 0

    while len(truncatable_prime_set) < 11:
        for start in "2357":
            for end in "37":
                for p in product("1379", repeat=num_repeat):
                    this_n_str = start + "".join(p) + end
                    this_n = int(this_n_str)

                    if is_truncatable_prime(this_n_str):
                        truncatable_prime_set.add(this_n)
                        result += this_n

        num_repeat += 1

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
