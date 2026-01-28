def main():
    with open("2025/03/input.txt", "r") as f:
        data = f.read().strip().split("\n")
    
    total_joltage = 0
    for bank in data:
        digits = []
        search_start = 0
        for digit_number in range(12):
            for current_digit in range(9, 0, -1):
                pos = bank.find(str(current_digit), search_start)
                if 0 <= pos <= len(bank) - (12 - digit_number):
                    digits.append(str(current_digit))
                    search_start = pos + 1
                    break
        joltage = int("".join(digits))
        total_joltage += joltage
    
    print(total_joltage)


if __name__ == "__main__":
    main()