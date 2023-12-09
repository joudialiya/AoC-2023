import re

def solution():
    with open("input") as file:
        lines = file.readlines()
        instractions = lines[0].strip()
        nodes = {}
        current = "AAA"
        for i, line in enumerate(lines):
            if i > 1:
                (node, left, right) = re.search("(\w\w\w) = \((\w\w\w), (\w\w\w)\)", line).groups()
                nodes[node] = {"left": left, "right": right}
        found = False
        index = 0
        print(current, len(instractions), len(nodes))
        while (not found):
            # print(current)
            # print(index, index % len(instractions))
            if current == "ZZZ":
                found = True
            else:
                if instractions[index % len(instractions)] == "L":
                    current = nodes[current]["left"]
                else:
                    current = nodes[current]["right"]
                index += 1
        return index
if __name__ == "__main__":
    print(solution())
