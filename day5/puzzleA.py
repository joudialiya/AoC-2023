def solution():
    with open("sample", "r") as file:
        lines = file.readlines()
        seeds = None
        maps = []
        title = None
        index = -1

        for i, line in enumerate(lines):
            if i == 0:
                seeds = [int(seed) for seed in line.split(':')[1].strip().split()]
            else:
                if line[0].isalpha():
                    index += 1
                    title = line.strip()[:-1]
                    maps.append({
                        "title": title,
                        "entries": []
                    })
                elif not line[0].isspace():
                    start_dest, start_src, length = line.strip().split()

                    maps[index]["entries"].append({
                        "destination": int(start_dest),
                        "source": int(start_src),
                        "length": int(length)
                    })
        print(maps)
        min = None
        for seed in seeds:
            value = seed
            for layer in maps:
                found = False
                for entry in layer["entries"]:
                    if (value >= entry["source"] and
                        value <= entry["source"] + entry["length"]):
                        value = entry["destination"] + value - entry["source"]
                        found = True
                        break
            if (min == None or min > value):
                min = value
            print(value)
    return min

if __name__ == "__main__":
    print("min:", solution())
