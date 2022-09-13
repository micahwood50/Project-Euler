def isPalindrome(n: int) -> bool:
    sn = str(n)
    return sn == sn[::-1]

def main():
    result = 0

    for ni in range(999, 100, -1):
        for nj in range(ni, 100, -1):
            if isPalindrome(ni*nj):
                result = max(result, ni*nj)

    print(f"Answer is {result}")

if __name__ == "__main__":
    main()
