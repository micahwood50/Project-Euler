from sympy.solvers.diophantine.diophantine import diop_DN


def main():
    result = 0
    max_x = 0

    for D in range(2, 1_001):
        this_x = diop_DN(D, 1)[0][0]
        if this_x > max_x:
            max_x = this_x
            result = D

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
