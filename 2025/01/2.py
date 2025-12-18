def main():
    with open("2025/01/input.txt", "r") as f:
        data = f.read().strip().split("\n")
    
    instructions = ((x[0], int(x[1:])) for x in data)

    pos = 50
    zeros = 0

    for (dir, val) in instructions:
        if dir == "R":
            pos += val
            zeros += pos // 100
            pos = pos % 100
        else:
            if pos == 0:
                pos = 100
            pos -= val
            zeros += (100-pos) // 100
            pos = pos % 100
        pass

    print(zeros)


if __name__ == "__main__":
    main()