from itertools import product


def square_distance(pa: tuple[int, int], pb: tuple[int, int]) -> int:
    xa, ya = pa
    xb, yb = pb

    return (xb - xa) ** 2 + (yb - ya) ** 2


def main():
    result = 0
    P0 = (0, 0)

    for x1, y1, y2 in product(range(51), repeat=3):
        for x2 in range(x1 + 1):
            P1 = (x1, y1)
            P2 = (x2, y2)

            if P1 < P2 or len(set([P0, P1, P2])) != 3:
                continue

            d01 = square_distance(P0, P1)
            d02 = square_distance(P0, P2)
            d12 = square_distance(P1, P2)

            ds, dm, dl = sorted([d01, d02, d12])

            if ds + dm == dl:
                result += 1

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
