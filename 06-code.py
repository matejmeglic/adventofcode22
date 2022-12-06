# find beginning of the signal
# https://adventofcode.com/2022/day/6

with open('06-input.txt', 'r', encoding="utf-8") as signalList:
    # part 1
    for signal in signalList:
        counter = 4
        while counter <= len(signal):
            signalString = signal[(counter-4):counter]
            checkString = ''
            for character in signalString:
                checkString += str(signalString.index(character))
            if checkString == '0123':
                print(counter)
                break

            counter += 1

    # part 2 - find 14 distinct chars
with open('06-input.txt', 'r', encoding="utf-8") as signalList:
    for signal in signalList:
        counter = 14
        while counter <= len(signal):
            signalString = signal[(counter-14):counter]
            checkString = ''
            for character in signalString:
                checkString += str(signalString.index(character))
            if checkString == '012345678910111213':
                print(counter)
                break

            counter += 1
    # why part 2 doesn't work like that? Why do I have to reimport the file?
