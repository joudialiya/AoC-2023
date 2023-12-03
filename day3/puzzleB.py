def search(y: int, x: int, map):
    start = x
    end = x
    while (start >= 0 and map[y][start].isdigit()):
        start -= 1
    while (end < len(map[0]) and map[y][end].isdigit()):
        end += 1
    return ((start + 1, end, y))
def solution():
    with open("input", "r") as file:
        lines = file.readlines()
        lines = [line.replace("\n", ".") for line in lines]
        sum = 0
        for y, line in enumerate(lines):
            for x, value in enumerate(line):
                if not value.isdigit() and value == '*':
                    # search around it for a digit
                    nParts = 0
                    parts = [] 
                    # top
                    if y > 0 and lines[y - 1][x].isdigit():
                        nParts += 1
                        if x == 87 and y == 2:
                            print("top") 
                        parts.append(search(y - 1, x, lines))
                    # bottom
                    if y < len(lines) - 1 and lines[y + 1][x].isdigit():
                        nParts += 1
                        if x == 87 and y == 2:
                            print("bottom") 
                        parts.append(search(y + 1, x, lines))
                    # left
                    if x > 0 and lines[y][x - 1].isdigit():
                        nParts += 1
                        if x == 87 and y == 2:
                            print("left") 
                        parts.append(search(y, x - 1, lines))
                    # right
                    if x < len(line) - 1 and lines[y][x + 1].isdigit():
                        nParts += 1
                        if x == 87 and y == 2:
                            print("right") 
                        parts.append(search(y, x + 1, lines))
                    # top-left
                    if (y > 0 and
                        x > 0 and
                        lines[y - 1][x - 1].isdigit()):
                        nParts += 1
                        if x == 87 and y == 2:
                            print("top-left") 
                        parts.append(search(y - 1, x - 1, lines))
                    # botoom-left
                    if (y < len(lines) - 1 and
                        x > 0 and
                        lines[y + 1][x - 1].isdigit()):
                        nParts += 1
                        if x == 87 and y == 2:
                            print("bottom-left") 
                        parts.append(search(y + 1, x - 1, lines))
                    # top-right
                    if (y > 0 and
                        x < len(line) - 1 and
                        lines[y - 1][x + 1].isdigit()):
                        nParts += 1
                        if x == 87 and y == 2:
                            print("top-right") 
                        parts.append(search(y - 1, x + 1, lines))
                    # bottom-right
                    if (y < len(lines) - 1 and
                        x < len(line) - 1 and
                        lines[y + 1][x + 1].isdigit()):
                        nParts += 1
                        if x == 87 and y == 2:
                            print("bottom-right") 
                        parts.append(search(y + 1, x + 1, lines))
                    parts = list(set(parts))
                    if len(parts) == 2:
                        partNumbers = [int(lines[row][start: end]) for start, end, row in parts]
                        print(partNumbers, partNumbers[0] * partNumbers[1])
                        sum += partNumbers[0] * partNumbers[1]
                    else:
                        print (nParts, x, y)
    return sum
if __name__ == "__main__":
    print(solution())
