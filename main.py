"""Main Module
Dave Smith
Key Technology, Programming Exercise"""

# Problem Statement: given a 2D field of asteroids, find the asteroid with the smallest viewing
# angle that contains the rest of the asteroid field. Input will be a text file containing:
#
# the number of asteroids on the first line (integer)
# on each new line thereafter, the listed location of  each asteroid by 2D coordinates

import sys
import asteroid_scanner


def main():
    """Main"""
    try:
        input_file = sys.argv[1]
    except(OSError, IOError):
        print('Must supply asteroid input file')
        sys.exit()
    # Get list of asteroids.
    ast_list = asteroid_scanner.AsteroidScanner.import_asteroids(input_file)

    # Scan for best 'viewing' asteroid
    best_asteroid = asteroid_scanner.AsteroidScanner.scan(ast_list)

    if best_asteroid is not None:
        print(f'{best_asteroid[0]} {best_asteroid[1]}')


if __name__ == '__main__':
    main()
