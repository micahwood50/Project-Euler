def convert_to_words(number: int, zeroFlag: bool = True) -> str:
    number_words = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
        100: "hundred",
        1000: "thousand",
    }

    if number == 0:
        return "zero" if zeroFlag else ""
    if number < 0:
        return "minus " + convert_to_words(-number)
    if number < 21:
        return number_words[number]
    if number < 100:
        return (
            number_words[number // 10 * 10] + " " + convert_to_words(number % 10, False)
        )
    if number < 1000:
        return (
            number_words[number // 100]
            + " "
            + number_words[100]
            + (" and " if number % 100 else "")
            + convert_to_words(number % 100, False)
        ).strip()
    for i, k in enumerate(number_words):
        if number < 1000 ** (i + 1):
            return (
                number_words[number // 1000**i]
                + " "
                + number_words[1000**i]
                + " "
                + convert_to_words(number % 1000**i, False)
            ).strip()


def count_letters(s: str) -> int:
    result = 0
    for ch in s:
        if ch.isalpha():
            result += 1

    return result


def main():
    result = 0

    for n in range(1, 1_001):
        result += count_letters(convert_to_words(n))

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
