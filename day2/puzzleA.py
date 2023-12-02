colorToNumber = {}
colorToNumber["green"] = 13
colorToNumber["red"] = 12
colorToNumber["blue"] = 14
def solution():
    with open("input", "r") as file:
        gameIDsSum = 0
        lines = file.readlines()
        for i, line in enumerate(lines):
            valid  = True
            # extract the games
            game = line.split(':')[1]
            game = game.strip()
            # extract the sets
            sets = game.split(';')
            # transform  the set into a map dict repr
            for set in sets:
                cubes = set.split(',')
                for cube in cubes:
                    print(cube)
                    cube = cube.strip()
                    number, color = cube.split(' ')
                    if (int(number) > colorToNumber[color]):
                        valid = False
                        break
                if not valid:
                    break
            if valid:
                gameIDsSum += i + 1

    return gameIDsSum

if __name__ == "__main__":
    print(solution())
