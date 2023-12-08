def solution():
    with open("input", "r") as file:
        period, dictanceToBeat = [
            int(line.split(":")[1].replace(" ", "")) for line in file.readlines()]
        print(period, dictanceToBeat)

        count = 0
        for tick in range(0, period):
            distance = tick * (period - tick)
            if distance > dictanceToBeat:
                count += 1
        return (count)

if __name__ == "__main__":
    print(solution())