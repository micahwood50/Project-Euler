from play import compare_hand_strings, Hand

FILENAME = "input.txt"


def get_input() -> list[list[str]]:
    hands_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            hands_list.append(line.strip().split())

    return hands_list


def main():
    hands_list = get_input()
    result = 0

    for hands in hands_list:
        player1_hand = " ".join(hands[:5])
        player2_hand = " ".join(hands[5:])
        if compare_hand_strings(player1_hand, player2_hand) == Hand.WIN:
            result += 1

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
