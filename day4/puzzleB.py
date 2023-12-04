
import math
def getWinningNumsCount(index, games):
    winningNumsCount = 0
    myNums, winningNums = games[index].split('|')

    myNums = myNums.split(' ')
    myNums = filter(lambda num: num != '', myNums)
    myNums = [int(num) for num in myNums]
    
    winningNums = winningNums.split(' ')
    winningNums = filter(lambda num: num != '', winningNums)
    winningNums = [int(num) for num in winningNums]

    winningNumsCount = 0
    for num in myNums:
        if num in winningNums:
            winningNumsCount += 1
    return winningNumsCount

def solution():
    with open("input", "r") as file:
        lines = file.readlines()
        games = [line.split(':')[1].strip() for line in lines]
        totalCartds = 0
        cardsCount = [1 for line in lines]

        for gameIndex, game in enumerate(games):
            winningNumsCount = getWinningNumsCount(gameIndex, games)
            totalCartds += cardsCount[gameIndex]
            print(gameIndex, winningNumsCount, cardsCount)
            if winningNumsCount > 0:
                for i in  range(1, winningNumsCount + 1):
                    if i + gameIndex < len(games):
                        cardsCount[i + gameIndex] += 1 * cardsCount[gameIndex]
    return totalCartds
if __name__ == "__main__":
    print(solution())
