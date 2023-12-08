def solution():
    with open("input", "r") as file:
        lines = file.readlines()
        lines = [line.split(":")[1].strip() for line in lines]
        timePeriods = filter(
            lambda num: num != '',
            [num for num in lines[0].split(' ')])
        distances = filter(
            lambda num: num != '',
            [num for num in lines[1].split(' ')])
        timePeriods = [int(num) for num in timePeriods]
        distances = [int(num) for num in distances]
        print(timePeriods, distances)
        
        result = 1
        for i in range(0, len(distances)):
            print("----", timePeriods[i])

            count = 0
            for tick in range(0, timePeriods[i]):
                distance = tick * (timePeriods[i] - tick)
                #print(tick, distance)
                if distance > distances[i]:
                    count += 1
            result *= count
            #print(i , "count:", count)
        return result
        pass

if __name__ == "__main__":
    print(solution())