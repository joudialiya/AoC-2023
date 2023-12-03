
def solution():
    with open("input", "r") as file:
        lines = file.readlines()
        print(len(lines), len(lines[0]))
        lines = [line.replace("\n", ".") for line in lines]
        print(len(lines), len(lines[0]))
        sum = 0
        for y, line in enumerate(lines):
            beginning = 0
            end = 0
            numberFound = False
            for x, value in enumerate(line):
                if value.isdigit():
                    print(value)
                    if not numberFound:
                        numberFound = True
                        beginning = x
                        end = x
                    else:
                        end = x
                else:
                    if numberFound == True:
                        """
                        i extract the number value 
                        and i check if a sumbole is present in it primeter
                        """
                        numberFound = False
                        symboleFound = False
                        for i in range(beginning, end + 1):
                            if y > 0 and not lines[y - 1][i].isdigit() and not lines[y - 1][i] == '.':
                                symboleFound = True
                                break
                            if y < len(lines) - 1 and not lines[y + 1][i].isdigit() and not lines[y + 1][i] == '.':
                                symboleFound = True
                                break

                            if i > 0 and not line[i - 1].isdigit() and not line[i - 1] == '.':
                                symboleFound = True
                                break
                            if (y > 0 and
                                i > 0 and
                                not lines[y - 1][i - 1].isdigit() and
                                not lines[y - 1][i - 1] == '.'):
                                symboleFound = True
                                break
                            if (y < len(lines) - 1 and
                                i > 0 and
                                not lines[y + 1][i - 1].isdigit() and
                                not lines[y + 1][i - 1] == '.'):
                                symboleFound = True
                                break

                            if i < len(line) - 1 and not line[i + 1].isdigit() and not line[i + 1] == '.':
                                symboleFound = True
                                break
                            if (y > 0 and
                                i < len(line) - 1 and
                                not lines[y - 1][i + 1].isdigit() and
                                not lines[y - 1][i + 1] == '.'):
                                symboleFound = True
                                break
                            if (y < len(lines) - 1 and
                                i < len(line) - 1 and
                                not lines[y + 1][i + 1].isdigit() and
                                not lines[y + 1][i + 1] == '.'):
                                symboleFound = True
                                break
                        print(int(line[beginning: x]), symboleFound)
                        if symboleFound:
                            sum += int(line[beginning: x])
    return sum
if __name__ == "__main__":
    print(solution())
