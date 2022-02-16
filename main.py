# Dave Smith
# Key Technology, Programming Exercise

# Problem Statement: given a 2D field of asteroids, find the asteroid with the smallest viewing angle that contains the
# rest of the asteroid field. Input will be a text file containing:
#
# the number of asteroids on the first line (integer)
# on each new line thereafter, the listed location of  each asteroid by 2D coordinates

import asteroid_scanner


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    inputFile = 'input.txt'
    # Get list of asteroids.
    astList = asteroid_scanner.importAsts(inputFile)

    # Scan for best 'viewing' asteroid
    bestAst = asteroid_scanner.scan(astList)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
