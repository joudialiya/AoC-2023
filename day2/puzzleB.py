colorToNumber = {}
colorToNumber["green"] = 13
colorToNumber["red"] = 12
colorToNumber["blue"] = 14
def solution():
    with open("input", "r") as file:
        sumSetsPower = 0
        lines = file.readlines()
        for i, line in enumerate(lines):
            minColorNumber = {}
            minColorNumber["green"] = 0
            minColorNumber["red"] = 0
            minColorNumber["blue"] = 0

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
                    if int(number) > minColorNumber[color]:
                        minColorNumber[color] = int(number)
            setPower = minColorNumber["red"]
            setPower *= minColorNumber["green"] 
            setPower *= minColorNumber["blue"]
            sumSetsPower += setPower

    return sumSetsPower

if __name__ == "__main__":
    print(solution())
