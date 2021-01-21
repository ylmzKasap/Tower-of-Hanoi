import os
import copy

NUMBER_OF_DISKS = 5

disks = [i+1 for i in range(NUMBER_OF_DISKS)]
startingPosition = [[i, 0, 0] for i in range(NUMBER_OF_DISKS+1)]
possibleMoves = ['AB', 'AC', 'BA', 'BC', 'CA', 'CB']
rodNumber = {'A': 0, 'B': 1, 'C': 2}


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
    print('A'.center(24), 'B'.center(24), 'C'.center(22), '\n')


def landing_area_loop(positionList):
    landingArea = 0
    for row in positionList:
        if row != 0:
            return row, landingArea - 1
        landingArea += 1
    return 0, landingArea - 1


def get_landing_area(positionList):
    A = [positionList[i][0] for i in range(len(positionList))]
    B = [positionList[i][1] for i in range(len(positionList))]
    C = [positionList[i][2] for i in range(len(positionList))]

    topA, landingA = landing_area_loop(A)
    topB, landingB = landing_area_loop(B)
    topC, landingC = landing_area_loop(C)

    return topA, topB, topC, landingA, landingB, landingC


def player_move(move, positionList):
    topA, topB, topC, landingA, landingB, landingC = get_landing_area(positionList)
    topDisks = {'A': topA, 'B': topB, 'C': topC}
    landingArea = {'A': landingA, 'B': landingB, 'C': landingC}

    if topDisks[move[0]] == 0:
        return 'NoDiskError', topDisks[move[0]], topDisks[move[1]]
    elif topDisks[move[1]] != 0:
        if topDisks[move[0]] > topDisks[move[1]]:
            return 'DiskError', topDisks[move[0]], topDisks[move[1]]
    elif topDisks[move[0]] == topDisks[move[1]]:
        return 'EmptyDiskError', topDisks[move[0]], topDisks[move[1]]

    positionList[landingArea[move[1]]][rodNumber[move[1]]] = topDisks[move[0]]
    positionList[landingArea[move[0]] + 1][rodNumber[move[0]]] = 0
    return positionList, topDisks[move[0]], topDisks[move[1]]


def let_the_game_begin(positionList):
    print('\nWelcome to Tower of Hanoi.')
    print('Move the entire stack of disks to another rod to win the game.')
    print("\nSample move: Typing 'AB' moves the top disk on rod A to rod B")

    while True:
        print('\nEnter a move.')
        print_position(positionList)
        playerMove = input()
        if playerMove not in possibleMoves:
            os.system('cls')
            print(f"\nThere is no such move called {playerMove}. Possible moves are:\n{', '.join(possibleMoves)}")
            continue

        moveResult, topDisk1, topDisk2 = player_move(playerMove, positionList)
        if moveResult == 'DiskError':
            print(
                f'\nIncorrect move, top disk in {playerMove[0]}({topDisk1})'
                f' is larger than {playerMove[1]}({topDisk2}).')
        elif moveResult == 'EmptyDiskError':
            print('\nIncorrect move, both rods are empty.')
        elif moveResult == 'NoDiskError':
            print(f'\nThere is no disk to move in {playerMove[0]}.')
        else:
            positionList = moveResult


let_the_game_begin(startingPosition)
