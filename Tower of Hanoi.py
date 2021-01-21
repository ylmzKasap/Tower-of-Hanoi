import os

NUMBER_OF_DISKS = 5

disks = [i+1 for i in range(NUMBER_OF_DISKS)]
startingPosition = [[i, 0, 0] for i in range(NUMBER_OF_DISKS+1)]
possibleMoves = ['AB', 'AC', 'BA', 'BC', 'CA', 'CB']
rodNumber = {'A': 0, 'B': 1, 'C': 2}


def format_position(positionList):
    for i, item in enumerate(positionList):
        for ii, subItem in enumerate(item):
            if subItem == 0:
                positionList[i][ii] = '||'
            else:
                positionList[i][ii] = f'_{subItem}'.center((subItem * 2) + 2, '@')
    return positionList


def print_position(positionList):
    positionList = format_position(positionList)

    print()
    for rowList in positionList:
        for row in rowList:
            print(str(row).center(24), end='')
        print()
    print('A'.center(24), 'B'.center(24), 'C'.center(22), '\n')


def landing_area_loop(list):
    landingArea = 0
    for row in list:
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
    if move not in possibleMoves:
        print(f"\nThere is no such move called {move}. Possible moves are:\n{', '.join(possibleMoves)}")
        print()
    topA, topB, topC, landingA, landingB, landingC = get_landing_area(positionList)
    topDisks = {'A': topA, 'B': topB, 'C': topC}

    if topDisks[move[0]] < topDisks[move[1]]:
        print(
            f'\nIncorrect move, top disk in {move[0]}({topDisks[move[0]]})'
            f' is smaller than {move[1]}({topDisks[move[1]]}).')
    elif topDisks[move[0]] == topDisks[move[1]]:
        print('\nIncorrect move, both rods are empty.')

    
inp = 'AC'
player_move(inp, startingPosition)

for i in startingPosition:
    print(i)
