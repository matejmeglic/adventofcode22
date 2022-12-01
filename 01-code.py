# find the elf with the most calories from the list

with open('01-list.txt', 'r', encoding="utf-8") as calories_list:
    caloriesCounter = {}
    elfCalories = 0
    iterationCounter = 1

    # calculate calories per elf
    for line in calories_list:
        if line != "\n":
            elfCalories += int(line)
        else:
            caloriesCounter[iterationCounter] = elfCalories
            elfCalories = 0
            iterationCounter += 1

    if elfCalories != 0:
        caloriesCounter[iterationCounter] = elfCalories

    print(caloriesCounter)
    print(
        f'The most loaded elf is elf number {max(caloriesCounter, key=caloriesCounter.get)} with {caloriesCounter[max(caloriesCounter, key=caloriesCounter.get)]} calories.')
