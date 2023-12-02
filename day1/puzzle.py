digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'] 
def solution():
    with open("input", "r") as file:

        lines = file.readlines()
        sum = 0
        for i, line in enumerate(lines):
            number = ""
            first = 0
            last = 0
            iFirst = len(line)
            iLast = 0
            # search for the first and last digit [0-9]
            for j, char in enumerate(line):
                if char.isdigit():
                    iFirst = j
                    first = ord(char) - ord('0')
                    break
            for j, char in enumerate(line):
                if char.isdigit():
                    iLast = j
                    last = ord(char) - ord('0')

            # serach for the first and last digit in word form and updated it if
            # it occure before the ifirst and after the ilast
            for k, word in enumerate(digits):    
                iFirstWord = line.find(word)
                iLastWord = line.rfind(word)
                if iFirstWord != -1 and iFirstWord < iFirst:
                    iFirst = iFirstWord
                    first = k + 1
                if iLastWord != -1 and iLastWord > iLast:
                    iLast = iLastWord
                    last = k + 1
            sum += first * 10 + last
    return sum

if __name__ == "__main__":
    print(solution())
