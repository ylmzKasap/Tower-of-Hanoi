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


def get_top_disk(positionList):
    A = [positionList[i][0] for i in range(len(positionList))]
    B = [positionList[i][1] for i in range(len(positionList))]
    C = [positionList[i][2] for i in range(len(positionList))]
    topA, topB, topC = max(A), max(B), max(C)
    return topA, topB, topC

# TODO get_landing_area


def player_move(move, positionList):
    if move not in possibleMoves:
        print(f"\nThere is no such move called {move}. Possible moves are:\n{', '.join(possibleMoves)}")
        print()
    A, B, C = get_top_disk(positionList)

    if eval(move[0]) < eval(move[1]):
        print(
            f'\nIncorrect move, top disk in {move[0]}({eval(move[0])})'
            f' is smaller than {move[1]}({eval(move[1])}).')
    elif eval(move[0]) == eval(move[1]):
        print('\nIncorrect move, both rods are empty.')

    
inp = 'BA'
player_move(inp, startingPosition)

for i in startingPosition:
    print(i)
