FILENAME = "input.txt"

def get_input() -> int:
    with open(FILENAME) as file:
        num = int(file.readline())

    return num

def main():
    num = get_input()

    result = 0

    for n in range(num):
        if n % 3 == 0 or n % 5 == 0:
            result += n

    print(f"Answer is {result}")

if __name__ == "__main__":
    main()
