# find overlapping pairs
# https://adventofcode.com/2022/day/4


overlappingPairs = 0

with open('04-input.txt', 'r', encoding="utf-8") as inputList:
    for pair in inputList:
        pair = pair.strip().split(",")
        elfOne = pair[0].split("-")
        elfTwo = pair[1].split("-")
        if int(elfOne[0]) <= int(elfTwo[0]):
            if int(elfOne[1]) >= int(elfTwo[1]):
                overlappingPairs += 1
                continue
        if int(elfTwo[0]) <= int(elfOne[0]):
            if int(elfTwo[1]) >= int(elfOne[1]):  # f* integers
                overlappingPairs += 1
                continue

    print(overlappingPairs)

# part 2 - basic (not total) overlap
overlappingPairs = 0

with open('04-input.txt', 'r', encoding="utf-8") as inputList:
    for pair in inputList:
        overlappingPairs += 1
        pair = pair.strip().split(",")
        elfOne = pair[0].split("-")
        elfTwo = pair[1].split("-")
        # exclude only pairs with NO overlap
        if int(elfOne[0]) < int(elfTwo[0]):
            if int(elfOne[1]) < int(elfTwo[0]):
                overlappingPairs -= 1
                continue
        if int(elfOne[0]) > int(elfTwo[1]):
            if int(elfOne[1]) > int(elfTwo[1]):
                overlappingPairs -= 1
                continue

    print(overlappingPairs)
