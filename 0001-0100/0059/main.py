from itertools import product

FILENAME = "input.txt"


def get_input() -> list[int]:
    byte_list = list()

    with open(FILENAME) as file:
        byte_list.extend(map(int, file.readline().strip().split(",")))

    return byte_list


def main():
    byte_list = get_input()
    result = 0
    max_E_count = 0
    result_message = ""

    for pw_bytes in product(range(ord("a"), ord("z") + 1), repeat=3):
        pw = "".join(map(chr, pw_bytes))
        ascii_list = [chr(byte ^ (pw_bytes[i % 3])) for i, byte in enumerate(byte_list)]

        original_message = "".join(ascii_list)
        count_e = original_message.lower().count("e")

        if count_e > max_E_count:
            result_message = original_message
            max_E_count = count_e

    result = sum(map(ord, result_message))

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
