import re
import math

def solution():
    with open("input") as file:
        lines = file.readlines()
        instractions = lines[0].strip()
        nodes = {}
        currents = []
        for i, line in enumerate(lines):
            if i > 1:
                (node, left, right) = re.search("(\w\w\w) = \((\w\w\w), (\w\w\w)\)", line).groups()
                nodes[node] = {"left": left, "right": right}
        for key in nodes.keys():
            if key[2] == "A":
                currents.append(key)
        
        index = 0
        print(currents, len(instractions), len(nodes))
        indecies = []
        for current in currents:
            found = False 
            index = 0
            while current[2] != "Z":
                if instractions[index % len(instractions)] == "L":
                    current = nodes[current]["left"]
                else:
                    current = nodes[current]["right"]
                index += 1
            indecies.append(index)
        print(currents, indecies)
        return index
if __name__ == "__main__":
    print(solution())
    """To calculate the PGCM of the result numbers"""
    # https://calculis.net/ppcm#2
