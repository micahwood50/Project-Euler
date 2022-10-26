def isDivisibleByAll20(n: int) -> bool:
  return all(n%i == 0 for i in range(2, 21))

def main():
    result = 2520
    
    while not isDivisibleByAll20(result):
        result += 20

    print(f"Answer is {result}")

if __name__ == "__main__":
    main()
