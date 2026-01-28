def main():
    with open("2025/03/input.txt", "r") as f:
        data = f.read().strip().split("\n")
    
    total_joltage = 0
    for bank in data:
        for dig_1 in range(9, -1, -1):
            pos = bank.find(str(dig_1))
            if pos not in [-1, len(bank)-1]:
                dig_2 = max(list(map(lambda x: int(x), bank[pos+1:])))
                total_joltage += dig_1*10 + dig_2
                break
    
    print(total_joltage)


if __name__ == "__main__":
    main()