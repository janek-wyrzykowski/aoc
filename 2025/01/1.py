def main():
    with open("input.txt", "r") as f:
        data = f.read().strip().split("\n")
    
    instructions = ((x[0], int(x[1:])) for x in data)

    pos = 50
    zeros = 0

    for (dir, val) in instructions:
        pos = (pos + (-val if dir == "L" else val)) % 100
        if pos == 0:
            zeros += 1

    print(zeros)


if __name__ == "__main__":
    main()