def solution():
    with open("input", "r") as file:
        lines = file.readlines()
        seeds = None
        maps = []
        title = None
        index = -1

        for i, line in enumerate(lines):
            if i == 0:
                # in part be we extart the pairs aka a range
                seeds = [int(seed) for seed in line.split(':')[1].strip().split()]
                ranges = []
                for i in range(0, len(seeds), 2):
                    ranges.append((seeds[i], seeds[i] + seeds[i + 1]))
                print(ranges)

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
        def linearInterpolation(ab, ai, cd):
            #print("..", ab, cd, ((cd[1] - cd[0]) / (ab[1] - ab[0])))
            return (cd[0] + (ai - ab[0]) * ((cd[1] - cd[0]) / (ab[1] - ab[0])))
        def process(r, layer):
            for entry in layer["entries"]:
                if (r[0] >= entry["source"] and
                    r[0] <= entry["source"] + entry["length"] and
                    r[1] >= entry["source"] and
                    r[1] <= entry["source"] + entry["length"]):
                    return [(
                        linearInterpolation(
                            (entry["source"], entry["source"] + entry["length"]),
                            r[0],
                            (entry["destination"], entry["destination"] + entry["length"])),

                        linearInterpolation(
                            (entry["source"], entry["source"] + entry["length"]),
                            r[1],
                            (entry["destination"], entry["destination"] + entry["length"])),
                    )]
                if (r[0] <= entry["source"] + entry["length"] and
                    r[1] > entry["source"] + entry["length"]):
                    # shop brom the end
                    t0 = (r[0], entry["source"] + entry["length"])
                    t1 = (entry["source"] + entry["length"] + 1, r[1])
                    return (process(t0, layer) + process(t1, layer))
                if (r[0] < entry["source"] and
                    r[1] >= entry["source"]):
                    # shop flm the start
                    t0 = (r[0], entry["source"] - 1)
                    t1 = (entry["source"], r[1])
                    return (process(t0, layer) + process(t1, layer))
            return [r]

        total_ranges = []
        for r in ranges:
            result_ranges = [r]
            print("initial range:", r)
            for layer in maps:
                output_ranges = []
                print(layer["title"])
                for inner_r in result_ranges:
                    output_ranges += process(inner_r, layer)
                    print("inner range:", output_ranges)
                result_ranges = output_ranges
            total_ranges += result_ranges

    return min(*[t[0]for t in total_ranges])

if __name__ == "__main__":
    print("min:", solution())
