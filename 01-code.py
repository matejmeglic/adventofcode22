with open('01-list.txt', 'r', encoding="utf-8") as topo_file:
    caloriesCounter = {}
    elfCalories = 0
    iterationCounter = 1

    for line in topo_file:
        if line != "\n":
            elfCalories += int(line)
        else:
            caloriesCounter[iterationCounter] = elfCalories
            elfCalories = 0
            iterationCounter += 1

    if elfCalories != 0:
        caloriesCounter[iterationCounter] = elfCalories

    print(
        f'The most loaded elf is elf number {max(caloriesCounter, key=caloriesCounter.get)} with {caloriesCounter[max(caloriesCounter, key=caloriesCounter.get)]} calories.')
