# Dave Smith
# Key Technology, Programming Exercise

# Problem Statement: given a 2D field of asteroids, find the asteroid with the smallest viewing
# angle that contains the rest of the asteroid field. Input will be a text file containing:
#
# the number of asteroids on the first line (integer)
# on each new line thereafter, the listed location of  each asteroid by 2D coordinates
import sys
import asteroid_scanner


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # try:
    #     inputFile = sys.argv[1]
    # except(OSError, IOError):
    #     print('Must supply asteroid input file')
    #     quit()
    INPUT_FILE = 'input\\input2.txt'
    # Get list of asteroids.
    astList = asteroid_scanner.importAsts(INPUT_FILE)

    bestAsteroid = tuple()
    if len(astList) == 0:
        print('No asteroids supplied')
    elif len(astList) < 3:
        # Trivial Solution
        bestAsteroid = astList[0]
    else:
        # Scan for best 'viewing' asteroid
        bestAst = asteroid_scanner.scan(astList)

    print('{0} {1}'.format(*bestAst))
