# count priority repeated letters between two elf rucksacks
# https://adventofcode.com/2022/day/3

import string
points = string.ascii_lowercase+string.ascii_uppercase

repeatedItemsCounter = 0

with open('03-input.txt', 'r', encoding="utf-8") as rucksacks:
    for line in rucksacks:
        itemsInLine = line.strip()
        rucksackOne = line[0:int(len(itemsInLine)/2)]
        rucksackTwo = line[int(len(itemsInLine)/2):]
        commonChars = ''.join(set(rucksackOne).intersection(rucksackTwo))
        # check my previous solution, why that didn't work?
        commonCharsPoints = points.index(commonChars)+1
        repeatedItemsCounter += commonCharsPoints

print(repeatedItemsCounter)

# part 2 - group elves in trios and find common denominator
repeatedItemsCounter = 0

dicsTrios = []
trioCounter = 1

with open('03-input.txt', 'r', encoding="utf-8") as rucksacks:
    trio = []
    # groups of 3
    for line in rucksacks:
        trio.append(line.split())  # why does this outputs array?
        if trioCounter < 3:
            trioCounter += 1
        else:
            dicsTrios.append(trio)
            trioCounter = 1
            trio = []  # could this sanitization be done cleaner?

    for group in dicsTrios:
        commonChars = ''.join(set(group[0][0]).intersection(
            group[1][0]).intersection(group[2][0]))
        commonCharsPoints = points.index(commonChars)+1
        repeatedItemsCounter += commonCharsPoints

print(repeatedItemsCounter)
