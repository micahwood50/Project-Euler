from typing import Callable


def u(n: int) -> int:
    return (
        1
        - n
        + n**2
        - n**3
        + n**4
        - n**5
        + n**6
        - n**7
        + n**8
        - n**9
        + n**10
    )


def get_simple_lagrange_polynomial(S: list[int]) -> Callable[[int], int]:
    coords = [(x, y) for x, y in enumerate(S, start=1)]

    def f(n):
        sum_result = 0
        for xi, yi in coords:
            term_result = yi
            for xm, __ in coords:
                if xm != xi:
                    term_result *= (n - xm) / (xi - xm)

            sum_result += term_result

        return round(sum_result)

    return f


def main():
    result = 0
    N = 12
    matrix = list()

    for i in range(1, N):
        f = get_simple_lagrange_polynomial([u(ni) for ni in range(1, i + 1)])
        matrix.append([f(n) for n in range(1, N)])

    for i in range(N - 2):
        result += matrix[i][i + 1]

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
