FILENAME = "input.txt"

NUM_TO_ROMAN = {
    1: "I",
    4: "IV",
    5: "V",
    9: "IX",
    10: "X",
    40: "XL",
    50: "L",
    90: "XC",
    100: "C",
    400: "CD",
    500: "D",
    900: "CM",
    1000: "M",
}

ROMANS_TO_NUM = {v: k for k, v in NUM_TO_ROMAN.items()}


def get_input() -> list[str]:
    string_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            string_list.append(line.strip())

    return string_list


def roman_to_integer(roman_str: str) -> int:
    result = 0

    for i in range(len(roman_str) - 1):
        if ROMANS_TO_NUM[roman_str[i + 1]] > ROMANS_TO_NUM[roman_str[i]]:
            result -= ROMANS_TO_NUM[roman_str[i]]
        else:
            result += ROMANS_TO_NUM[roman_str[i]]

    result += ROMANS_TO_NUM[roman_str[len(roman_str) - 1]]

    return result


def integer_to_roman(num: int) -> str:
    result = ""
    roman_num = sorted(NUM_TO_ROMAN.keys(), reverse=True)

    for n in roman_num:
        while n <= num:
            result += NUM_TO_ROMAN[n]
            num -= n

    return result


def main():
    roman_list = get_input()
    result = 0

    for roman_str in roman_list:
        original_len = len(roman_str)
        optimal_len = len(integer_to_roman(roman_to_integer(roman_str)))

        result += original_len - optimal_len

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
