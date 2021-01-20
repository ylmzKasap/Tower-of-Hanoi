import os

NUMBER_OF_DISKS = 5

disks = [i+1 for i in range(NUMBER_OF_DISKS)]

startingPosition = [[[0, 0, 0]], [
    [i+1, 0, 0] for i in range(NUMBER_OF_DISKS)]]


def format_position(position):
    for i, item in enumerate(position):
        for ii, subItem in enumerate(item):
            for iii, subSubItem in enumerate(subItem):
                if subSubItem == 0:
                    position[i][ii][iii] = '||'
                else:
                    position[i][ii][iii] = f'_{subSubItem}'.center(((subSubItem) * 2) + 2, '@')
    return position


def print_position(positionList):

    positionList = format_position(positionList)
    print()

    for rowList in positionList:
        for row in rowList:
            for index, rowItem in enumerate(row):
                print(str(rowItem).center(24), end='')
            print()
    print('A'.center(24), 'B'.center(24), 'C'.center(22), '\n')


print_position(startingPosition)
