def main():
    a = b = 1
    index = 1
    while len(str(a)) < 1_000:
        a, b = b, a+b
        index += 1

    print(f"Answer is {index}")
    

if __name__ == "__main__":
    main()
