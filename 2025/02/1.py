def main():
    with open("2025/02/input.txt", "r") as f:
        data = f.read().strip().split(",")

    ranges = [tuple(x.split("-")) for x in data]

    invalid_sum = 0

    for (start, end) in ranges:
        for id in range(int(start), int(end)+1):
            id_str = str(id)
            if len(id_str) % 2 == 0:
                id_left = id_str[:len(id_str)//2]
                id_right = id_str[len(id_str)//2:]
                if id_left == id_right:
                    invalid_sum += int(id_left + id_right)

    print(invalid_sum)

if __name__ == "__main__":
    main()