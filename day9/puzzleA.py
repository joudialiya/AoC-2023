def getNext(list: list):
    allZero = True
    for n in list:
        if n != 0:
            allZero = False
            break
    if allZero:
        return 0
    derived = []
    for i in range(1, len(list)):
        derived.append(list[i] - list[i - 1])

    return list[len(list) - 1] + getNext(derived)
        

def solution():
    with open("input", 'r') as file:
        lines = file.read().splitlines()
        values = [list(map(lambda n: int(n), line.split())) for line in lines]
        sum = 0
        for vector in values:
           sum += getNext(vector)
        return sum
if __name__ == "__main__":
    print(solution())
