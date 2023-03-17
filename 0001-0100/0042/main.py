FILENAME = "input.txt"


def get_input() -> list[str]:
    words = []

    with open(FILENAME) as file:
        for line in file.readlines():
            line = line[1:-1]
            words.extend(line.split('","'))

    return words


def get_word_score(word: str) -> int:
    score = 0

    for ch in word:
        score += ord(ch.upper()) - ord("A") + 1

    return score


def main():
    words = get_input()
    result = 0

    max_score = max(get_word_score(word) for word in words)
    triangle_nums = set()
    n = 1

    while (tn := n * (n + 1) // 2) <= max_score:
        triangle_nums.add(tn)
        n += 1

    for word in words:
        if get_word_score(word) in triangle_nums:
            result += 1

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
