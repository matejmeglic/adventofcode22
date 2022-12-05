# rearrange cases on a crane
# https://adventofcode.com/2022/day/5

one = ["Q", "S", "W", "C", "Z", "V", "F", "T"]
two = ["Q", "R", "B"]
three = ["B", "Z", "T", "Q", "P", "M", "S"]
four = ["D", "V", "F", "R", "Q", "H"]
five = ["J", "G", "L", "D", "B", "S", "T", "P"]
six = ["W", "R", "T", "Z"]
seven = ["H", "Q", "M", "N", "S", "F", "R", "J"]
eight = ["R", "N", "F", "H", "W"]
nine = ["J", "Z", "T", "Q", "P", "R", "B"]

# how do you rearrange that from the items AoC provided
dictKeys = {1: one, 2: two, 3: three, 4: four,
            5: five, 6: six, 7: seven, 8: eight, 9: nine}

with open('05-input.txt', 'r', encoding="utf-8") as craneMoves:
    for move in craneMoves:
        move = move.split()
        count = 1
        placementOrigin = dictKeys[int(move[3])]
        placementDestination = dictKeys[int(move[5])]

        # while count <= int(move[1]):
        #    crate = placementOrigin[-1]
        #    placementOrigin.pop()
        #    placementDestination.append(crate)
        #    count += 1

        # part 2, move multiple objects without changing order
        midArrangement = []
        while count <= int(move[1]):
            crate = placementOrigin[-1]
            placementOrigin.pop()
            midArrangement.append(crate)
            count += 1
        for crateRev in reversed(midArrangement):
            placementDestination.append(crateRev)

print("___")
print(one[-1])  # print better !!
print(two[-1])
print(three[-1])
print(four[-1])
print(five[-1])
print(six[-1])
print(seven[-1])
print(eight[-1])
print(nine[-1])
