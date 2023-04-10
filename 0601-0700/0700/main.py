def main():
    modN = 4503599627370517
    N = 1504170715041707

    result, curr_low, curr_high = N, N, N

    while curr_low > 0:
        this_value = (curr_low + curr_high) % modN

        if this_value < curr_low:
            result += this_value
            curr_low = this_value
        else:
            curr_high = this_value

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
