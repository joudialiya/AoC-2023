from functools import cmp_to_key
cardToValue = {
    "J": 0, "2": 1, "3": 2, "4": 3, "5": 4,
    "6": 5, "7": 6, "8": 7, "9": 8,
    "T": 9, "Q": 11, "K": 12, "A": 13
}
handsToValue = {
    "High card": 1,
    "One pair": 2,
    "Two pair": 3,
    "Three of a kind": 4,
    "Full house": 5,
    "Four of a kind": 6,
    "Five of a kind": 7
}
"""
To solve the part 2 of the puzzle i have to make a change in the
Type defining function, now the J cart can morph into other carts to maximzs
the hand type what i did is that iww select the existent cards using set()
then iterat throught the cards and count them type by type.
and use these intels to tell the hand type.
Now i did add a few lins the will detect the presence of Joker cards,
get there counts and add the count to the card type with the max count already
that way the hand type will get maximaized, that is the morph, it reflect it self
on the out put data that made the dicision.
"""
def whichHandType(hand: str):
    chars = list(set(hand))
    counts = [0 for char in chars]
    for i in range(0, len(chars)):
        counts[i] = hand.count(chars[i])
    if chars.count("J") != 0 and len(chars) != 1:
        jCount = counts[chars.index("J")]
        del counts[chars.index("J")]
        chars.remove("J")
        counts[counts.index(max(counts))] += jCount
        
    if len(chars) == 1:
        return "Five of a kind"
    if len(chars) == 2:
        if counts.count(4) == 1:
            return "Four of a kind"
        if counts.count(3) == 1:
            return "Full house"
    if len(chars) == 3:
        if counts.count(3) == 1:
            return "Three of a kind"
        else:
            return "Two pair"
    if len(chars) == 4:
        return "One pair"
    if len(chars) == 5:
        return "High card"
    pass

def compareHands(a, b) -> int:
    a = a[0]
    b = b[0]
    aType = whichHandType(a)
    bType = whichHandType(b)
    if aType != bType:
        if handsToValue[aType] > handsToValue[bType]:
            return 1
        elif handsToValue[aType] < handsToValue[bType]:
            return -1
    for i in range(0, len(a)):
        if a[i] != b[i]:
            if cardToValue[a[i]] > cardToValue[b[i]]:
                return 1
            elif cardToValue[a[i]] < cardToValue[b[i]]:
                return -1
    return 0
def solution():
    with open("input", "r") as file:
        hands = [
            (line.split(" ")[0], int(line.split(" ")[1].replace("\n", "")))for line in file.readlines()]
        def wrapUp(a, b):
            result = compareHands(a, b)
            return result
        sortedHands = sorted(hands, key=cmp_to_key(wrapUp))
        value = 0

        for rank, hand in enumerate(sortedHands):
            value += hand[1] * (rank + 1)
        return value
    pass
if __name__ == "__main__":
    print(solution())
    print(compareHands(("T55J5", 0),("KTJJT", 0)))
    print(compareHands(("KKKK2", 0),("JJJJJ", 0)))