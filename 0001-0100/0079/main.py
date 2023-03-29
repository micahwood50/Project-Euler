from collections import defaultdict
from pprint import pprint

FILENAME = "input.txt"


def get_input() -> set[int]:
    logins_set = set()

    with open(FILENAME) as file:
        for line in file.readlines():
            logins_set.add(int(line))

    return logins_set


def main():
    logins = get_input()
    graph = defaultdict(set)

    for login in logins:
        d3 = login % 10
        d2 = login // 10 % 10
        d1 = login // 100

        graph[d1].add(d2)
        graph[d1].add(d3)
        graph[d2].add(d3)

    # Printing the graph, it is clear that each digit was used once:

    list_graph = list(graph.items())
    list_graph.sort(key=lambda t: -len(t[1]))
    result = "".join(str(t[0]) for t in list_graph)
    result += str(list_graph[-1][1])[1]

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
