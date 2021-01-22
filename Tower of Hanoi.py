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
    positionListRaw = copy.deepcopy(positionList)
    for i, item in enumerate(positionListRaw):
        for ii, subItem in enumerate(item):
            if subItem == 0:
                positionListRaw[i][ii] = '||'
            else:
                positionListRaw[i][ii] = f'_{subItem}'.center((subItem * 2) + 2, '@')
    return positionListRaw


def print_position(positionList):
    positionList = format_position(positionList)

    print()
    for rowList in positionList:
        for row in rowList:
            print(str(row).center(24), end='')
        print()
    print('-1-'.center(24), '-2-'.center(24), '-3-'.center(22), '\n')


def landing_area_loop(positionList):
    landingArea = 0
    for row in positionList:
        if row != 0:
            return row, landingArea - 1
        landingArea += 1
    return 0, landingArea - 1


def get_landing_area(positionList) -> object:
    one = [positionList[i][0] for i in range(len(positionList))]
    two = [positionList[i][1] for i in range(len(positionList))]
    three = [positionList[i][2] for i in range(len(positionList))]

    topOne, landingOne = landing_area_loop(one)
    topTwo, landingTwo = landing_area_loop(two)
    topThree, landingThree = landing_area_loop(three)

    return topOne, topTwo, topThree, landingOne, landingTwo, landingThree


def player_move(move, positionList):
    topOne, topTwo, topThree, landingOne, landingTwo, landingThree = get_landing_area(positionList)
    topDisks = {'1': topOne, '2': topTwo, '3': topThree}
    landingArea = {'1': landingOne, '2': landingTwo, '3': landingThree}

    if len(move) == 1:
        if landingTwo == 0 or landingThree == 0:
            return 'win'
        return

    if topDisks[move[0]] == 0:
        print('\n' + f'There is no disk to move in -{move[0]}-'.center(75))
        return
    elif topDisks[move[1]] != 0:
        if topDisks[move[0]] > topDisks[move[1]]:
            print(
                '\n' + (f'Incorrect move, top disk in -{move[0]}- ({topDisks[move[0]]})'
                        + f' is larger than -{move[1]}- ({topDisks[move[1]]}).').center(75))
            return
    elif topDisks[move[0]] == topDisks[move[1]]:
        print('\n' + 'Incorrect move, both rods are empty.'.center(75))
        return

    positionList[landingArea[move[1]]][rodNumber[move[1]]] = topDisks[move[0]]
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

    while True:
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

    while True:
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
