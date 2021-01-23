import os
import copy
import sys

NUMBER_OF_DISKS = 5

disks = [i + 1 for i in range(NUMBER_OF_DISKS)]
startingPosition = [[i, 0, 0] for i in range(NUMBER_OF_DISKS + 1)]
possibleMoves = ['12', '13', '21', '23', '31', '32']
rodNumber = {'1': 0, '2': 1, '3': 2}
introduction = 0


def format_position(positionList):
    """Takes a numeric list and turns zeros into rods (||).
    It also formats each disk with '@'."""

    formattedList = copy.deepcopy(positionList)
    for i, item in enumerate(formattedList):
        for ii, subItem in enumerate(item):
            if subItem == 0:
                formattedList[i][ii] = '||'
            else:
                formattedList[i][ii] = f'_{subItem}'.center((subItem * 2) + 2, '@')
    return formattedList


def print_position(positionList):
    """Takes a formatted list and prints it by aligning the rods."""

    formattedList = format_position(positionList)

    print()
    for rowList in formattedList:
        for row in rowList:
            print(str(row).center(24), end='')
        print()
    print('-1-'.center(24), '-2-'.center(24), '-3-'.center(22), '\n')


def get_landing_area(positionList):
    """Takes a numeric list and returns the the length of top disks
    and the index of landing area in each rod."""

    one = [positionList[i][0] for i in range(len(positionList))]
    two = [positionList[i][1] for i in range(len(positionList))]
    three = [positionList[i][2] for i in range(len(positionList))]

    topOne, landingOne = landing_area_loop(one)
    topTwo, landingTwo = landing_area_loop(two)
    topThree, landingThree = landing_area_loop(three)

    return topOne, topTwo, topThree, landingOne, landingTwo, landingThree


def landing_area_loop(positionList):
    """A loop to shorten get_landing_area function."""

    landingArea = 0
    for row in positionList:
        if row != 0:
            return row, landingArea - 1
        landingArea += 1
    return 0, landingArea - 1


def player_move(move, positionList):
    """Checks whether the submitted move is valid and alters the position list."""

    topOne, topTwo, topThree, landingOne, landingTwo, landingThree = get_landing_area(positionList)
    topDisks = {'1': topOne, '2': topTwo, '3': topThree}
    landingArea = {'1': landingOne, '2': landingTwo, '3': landingThree}

    if len(move) == 1:
        if landingTwo == 0 or landingThree == 0:
            return 'win'
        return

    topDisk1, topDisk2 = topDisks[move[0]], topDisks[move[1]]

    if topDisk1 == 0:
        print('\n' + f'There is no disk to move in -{move[0]}-'.center(75))
        return
    elif topDisk2 != 0:
        if topDisk1 > topDisk2:
            print(
                '\n' + (f"Incorrect move, {'@' * topDisk1}_{topDisk1}{'@' * topDisk1}"
                        + f" is larger than {'@' * topDisk2}_{topDisk2}{'@' * topDisk2}.").center(75))
            return
    elif topDisk1 == topDisk2:
        print('\n' + 'Incorrect move, both rods are empty.'.center(75))
        return

    positionList[landingArea[move[1]]][rodNumber[move[1]]] = topDisk1
    positionList[landingArea[move[0]] + 1][rodNumber[move[0]]] = 0
    return positionList


def let_the_game_begin(positionList):
    print('\n' + 'Welcome to Tower of Hanoi.'.center(75))
    global introduction
    if introduction == 0:
        print('\n' + 'Move the entire stack of disks to another rod to win the game.'.center(75))
        print("Sample move: Typing '12' moves the top disk on rod -1- to rod -2-.".center(75))
        introduction = 1
    moveNumber = 0

    while True:  # Game loop. Each iteration increases the moveNumber by one.
        print('\n' + 'Enter a move.'.center(75) + '\n')
        print_position(positionList)

        if player_move('A', positionList) == 'win':
            break

        playerMove = input()
        os.system('cls')
        if playerMove not in possibleMoves:
            print('\n' + f"There is no such move called {playerMove}.".center(75),
                  '\n' + f"Possible moves are: {', '.join(possibleMoves)}".center(75))
            continue

        moveResult = player_move(playerMove, positionList)
        if moveResult is None:
            continue
        moveNumber += 1
        positionList = moveResult

    while True:  # Enter a decision to exit win loop.
        os.system('cls')
        print()
        print_position(positionList)
        print('\n' + f'Congratulations! You won in {moveNumber} moves.'.center(75))
        print('\n' + 'Press \'a\' to play again, \'q\' to exit.'.center(75))
        decision = input().lower()
        if decision == 'a':
            os.system('cls')
            let_the_game_begin(copy.deepcopy(startingPosition))
        elif decision == 'q':
            sys.exit()
        else:
            continue


let_the_game_begin(copy.deepcopy(startingPosition))
