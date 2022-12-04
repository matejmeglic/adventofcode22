# count priority repeated letters between two elf rucksacks
# https://adventofcode.com/2022/day/3

import string
points = string.ascii_lowercase+string.ascii_uppercase
print(points)

repeatedItemsCounter = 0

with open('03-input.txt', 'r', encoding="utf-8") as rucksacks:
    for line in rucksacks:
        itemsInLine = len(line) - line.count('\n')
        rucksackOne = line[:int(itemsInLine/2)]
        rucksackTwo = line[int(-itemsInLine/2):]
        commonChars = ''.join(set(rucksackOne).intersection(rucksackTwo))
        commonCharsPoints = points.rfind(commonChars)+1
        repeatedItemsCounter += commonCharsPoints

        print(commonChars)
        print(commonCharsPoints)
        print("___")

print(repeatedItemsCounter)
