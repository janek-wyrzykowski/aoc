def main():
    with open("2025/02/input.txt", "r") as f:
        data = f.read().strip().split(",")

    ranges = [tuple(x.split("-")) for x in data]

    invalid_sum = 0

    for (start, end) in ranges:
        for id in range(int(start), int(end)+1):
            id_str = str(id)
            for i in range(len(id_str)//2, 0, -1):
                rep_count = round(len(id_str)/i, 0)
                if rep_count == len(id_str)/i:
                    if id_str[:i]*int(rep_count) == id_str:
                        invalid_sum += id
                        break

    print(invalid_sum)

if __name__ == "__main__":
    main()