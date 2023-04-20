from collections import defaultdict
from math import gcd


def generate_Pythagorean_triples(
    max_length: int,
) -> dict[int, set[tuple[int, int, int]]]:
    triples = defaultdict(set)
    m = 2

    while m * m < max_length:
        n = 1
        while 2 * m * (m + n) <= max_length and n < m:
            if m % 2 != n % 2 and gcd(m, n) == 1:
                a = m * m - n * n
                b = 2 * m * n
                c = m * m + n * n

                triples[2 * m * (m + n)].add((a, b, c))

            n += 1
        m += 1

    for key in sorted(triples.keys(), reverse=True):
        for value in triples[key]:
            a, b, c = value
            multiplier = 2

            while key * multiplier <= max_length:
                triples[key * multiplier].add(
                    (multiplier * a, multiplier * b, multiplier * c)
                )

                multiplier += 1

    return triples


def main():
    result = 0
    triples = generate_Pythagorean_triples(1_500_000)

    for triples_list in triples.values():
        if len(triples_list) == 1:
            result += 1

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
