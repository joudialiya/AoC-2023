
import math
def solution():
    with open("input", "r") as file:
        lines = file.readlines()
        games = [line.split(':')[1].strip() for line in lines]

        totalValue = 0
        for game in games:
            myNums, winningNums = game.split('|')
            myNums = myNums.split(' ')
            myNums = filter(lambda num: num != '', myNums)
            myNums = [int(num) for num in myNums]
            
            winningNums = winningNums.split(' ')
            winningNums = filter(lambda num: num != '', winningNums)
            winningNums = [int(num) for num in winningNums]
            winningNumsCount = 0
            value = 1
            for num in myNums:
                if num in winningNums:
                    winningNumsCount += 1
            for i in range(1, winningNumsCount):
                value *=  2
            if winningNumsCount > 0:
                totalValue += value
                
    return totalValue
if __name__ == "__main__":
    print(solution())
