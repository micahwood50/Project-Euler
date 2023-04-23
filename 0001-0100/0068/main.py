from itertools import permutations as P


def main():
    solutions = set()

    for a, b, c, d, e, f, g, h, i, j in P(range(1, 11), 10):
        possible_solution = [a, b, c, d, c, e, f, e, g, h, g, i, j, i, b]

        if (
            a + b + c == d + c + e == e + f + g == g + h + i == b + i + j
            and len("".join(str(n) for n in possible_solution)) == 16
        ):
            external_nodes = [a, d, f, h, j]
            min_external_node = min(external_nodes)

            for external_node, index in zip(external_nodes, range(0, 13, 3)):
                if external_node == min_external_node:
                    this_solution = (
                        possible_solution[index:] + possible_solution[:index]
                    )
                    solutions.add("".join(map(str, this_solution)))
                    break

    print(f"Answer is {max(solutions)}")


if __name__ == "__main__":
    main()
