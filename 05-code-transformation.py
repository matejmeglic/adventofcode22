# additional file for array tranformation

blankLine = 1
areas = {}
with open('05-input-craneAreas.txt', 'r', encoding="utf-8") as input:
    mylist = [line.rstrip('\n') for line in input]
    # find blank line
    for line in mylist:
        charCounter = 0
        for char in line:
            if char != " ":
                charCounter += 1
        if charCounter == 0:
            break
        blankLine += 1

    # determine number of areas
    counter = 1
    for line in mylist:
        if counter == (blankLine-1):
            areasNumber = len(line.split())
        counter += 1
    createAreas = 1
    while createAreas <= areasNumber:
        areas[createAreas] = []
        createAreas += 1

    # position crates in areas
    for line in mylist:
        if blankLine > 2:
            charCounter = 1
            for char in line:
                if char != ' ':
                    if charCounter == 2:
                        areas[1].append(char)
                    if charCounter > 2 and (charCounter-2) % 4 == 0:
                        areas[((charCounter-2)/4)+1].append(char)
                charCounter += 1
        blankLine -= 1
    for areaArray in areas:
        areas[areaArray].reverse()

print(areas)

# NICE
