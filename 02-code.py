# follow the rock-paper-scisors strategy and count your points
# https://adventofcode.com/2022/day/2


with open('02-input.txt', 'r', encoding="utf-8") as strategy_guide:
    dictShapes = {'rock': 1, 'paper': 2, 'scissors': 3}
    dictPoints = {'loss': 0, 'draw': 3, 'win': 6}
    dictMoves = {'A': 'rock', 'B': 'paper', 'C': 'scissors',
                 'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
    dictMovesNew = {'A': 'rock', 'B': 'paper', 'C': 'scissors',
                    'X': 'loss', 'Y': 'draw', 'Z': 'win'}
    dictOutcomes = [
        ['rock', 'rock', 'draw'],
        ['rock', 'scissors', 'loss'],
        ['rock', 'paper', 'win'],
        ['paper', 'paper', 'draw'],
        ['paper', 'rock', 'loss'],
        ['paper', 'scissors', 'win'],
        ['scissors', 'scissors', 'draw'],
        ['scissors', 'paper', 'loss'],
        ['scissors', 'rock', 'win']
    ]

    pointsCounter = 0

    for line in strategy_guide:
        game = line.split()
        player1 = dictMoves[game[0]]
        player2 = dictMoves[game[1]]
        for entry in dictOutcomes:
            if entry[0] == player1:
                if entry[1] == player2:
                    outcome = entry[2]

        # pointsCounter += dictShapes[player2]+dictPoints[outcome]
        # print(dictShapes[player2]+dictPoints[outcome])

        # change in the game, X,Y,Z mean different things
        player1 = dictMovesNew[game[0]]
        player2 = dictMovesNew[game[1]]
        for entry in dictOutcomes:
            if entry[0] == player1:
                if entry[2] == player2:
                    outcome = entry[1]

        pointsCounter += dictShapes[outcome]+dictPoints[player2]
        # print(dictShapes[outcome]+dictPoints[player2])

    print(pointsCounter)

    pointsCounter = 0
