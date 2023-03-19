def main():
    Pn = Hn = 40755

    n_P = 165
    n_H = 143

    while True:
        n_H += 1
        Hn += 4 * n_H - 3

        while Hn > Pn:
            n_P += 1
            Pn += 3 * n_P - 2

        if Pn == Hn:
            print(f"Answer is {Hn}")
            return


if __name__ == "__main__":
    main()
