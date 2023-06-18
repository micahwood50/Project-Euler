from collections import defaultdict


def p3(n: int) -> int:
    return n * (n + 1) // 2


def p4(n: int) -> int:
    return n * n


def p5(n: int) -> int:
    return n * (3 * n - 1) // 2


def p6(n: int) -> int:
    return n * (2 * n - 1)


def p7(n: int) -> int:
    return n * (5 * n - 3) // 2


def p8(n: int) -> int:
    return n * (3 * n - 2)


def main():
    number_dict = defaultdict(list)
    result = 0

    for pi, pf in enumerate([p3, p4, p5, p6, p7, p8], start=3):
        n = 1
        i = 1
        while n < 10_000:
            if n >= 1_000:
                number_dict[n].append(pi)

            i += 1
            n = pf(i)

    start_num = set()
    end_num = set()

    for num in number_dict.keys():
        start_num.add(int(str(num)[:2]))
        end_num.add(int(str(num)[2:]))

    chain_set = start_num & end_num

    for k in list(number_dict.keys()):
        start, end = int(str(k)[:2]), int(str(k)[2:])

        if start not in chain_set or end not in chain_set or start == end:
            del number_dict[k]

    graph = defaultdict(set)
    possible_candidates = set()

    for k0 in number_dict.keys():
        for kf in number_dict.keys():
            if k0 == kf:
                continue

            if str(k0)[2:] == str(kf)[:2]:
                graph[k0].add(kf)

    def dfs(graph, marked, length, node_val):
        if length == 0:
            start = str(marked[0])[:2]
            end = str(marked[-1])[2:]
            if start == end:
                possible_candidates.add(marked)

            return

        for next_node in graph[node_val]:
            if next_node in marked:
                continue

            dfs(graph, marked + (next_node,), length - 1, next_node)

    for key in list(graph.keys()):
        dfs(graph, tuple(), 6, key)

    for candidate in possible_candidates:
        if 3 not in number_dict[candidate[0]]:
            continue

        this_set = set()
        this_list = list()
        for cc in candidate:
            if number_dict[cc] in this_list and len(number_dict[cc]) == 1:
                break

            this_list.append(number_dict[cc])
            for c in number_dict[cc]:
                this_set.add(c)

        else:
            if len(this_set) == 6:
                print(f"Answer is {sum(candidate)}")
                return


if __name__ == "__main__":
    main()
