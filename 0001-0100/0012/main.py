from sympy import divisors

def triangle_number(n: int) -> int:
    return n*(n+1) // 2

def main():
    n = 1

    while len(divisors(result := triangle_number(n))) < 500:
        n += 1

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
