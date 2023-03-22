from itertools import permutations, product

FILENAME = "input.txt"


def get_input() -> list[tuple[int, list[int]]]:
    problems = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            line = line.strip()

            ans, perm = line.split(":")
            ans = int(ans)
            perm = list(map(int, perm.split(",")))
            perm.sort()

            problems.append((ans, perm))

    return problems


def get_minimum_score(target_goal: int, list_num: list[int]) -> int:
    operators = ["+", "-", "*", "//"]
    original_permutations = []

    if len(set(list_num)) != len(list_num):
        for p_length in range(2, len(list_num) + 1):
            original_permutations.extend(list(set(permutations(list_num, r=p_length))))
    else:
        for p_length in range(2, len(list_num) + 1):
            original_permutations.extend(list(permutations(list_num, r=p_length)))

    original_permutations.sort(key=sum)

    for p in original_permutations:
        for ops in product(operators, repeat=len(p) - 1):
            p = list(p)
            ops = list(ops)

            for opi in product(*[list(range(i)) for i in range(len(p) - 1, 0, -1)]):
                this_p = p[:]
                this_ops = ops[:]

                for oi in opi:
                    n1 = this_p.pop(oi)
                    n2 = this_p.pop(oi)
                    o1 = this_ops.pop(oi)

                    if o1 == "//":
                        if n1 % n2 != 0:
                            break

                    this_term_result = eval(f"{n1}{o1}{n2}")

                    if this_term_result <= 0:
                        break

                    this_p.insert(oi, this_term_result)

                else:
                    if target_goal == this_p[0]:
                        return sum(p)

    return 0


def main():
    problems = get_input()
    result = 0
    S = [0]

    for i, problem in enumerate(problems, start=1):
        this_score = get_minimum_score(*problem)
        print(f"    #{i:0>3} => {this_score}")
        S.append(this_score)

    for n in range(1, len(S)):
        result += 3**n * S[n]

    print(f"Answer is {result % 1_005_075_251}")


if __name__ == "__main__":
    main()
