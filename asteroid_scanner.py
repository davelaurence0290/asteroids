# Class to house the asteroid scanning methods

import math


class AsteroidScanner:
    # Variable to store lowest-Y asteroid location
    __asteroid0 = tuple()

    # Setting __asteroid0
    @classmethod
    def setAsteroid0(cls, asteroid0):
        cls.__asteroid0 = asteroid0

    # function to calculate distance between two Asteroids
    # (square of distance will be sufficient for comparisons)
    @staticmethod
    def squareDistance(ast1, ast2):
        return (ast1[1]-ast2[1])**2 + (ast1[0]-ast2[0])**2

    # function to calculate Cross-Product
    # used to check orientation during algorithm progression, and to sort initial asteroid points by angle.
    @staticmethod
    def crossProduct(ast1, ast2, ast3):
        return (ast1[0] - ast3[0]) * (ast2[1] - ast3[1]) - \
                (ast1[1] - ast3[1])*(ast2[0] - ast3[0])

    # function for initial sort of asteroids according to their angle with asteroid0
    @classmethod
    def angleSort(cls, ast1, ast2):
        # using cross product to tell difference in angle
        # 'clockwise' (positive) crossProduct means ast2 has larger angle with x-axis
        # 'counter-clockwise' (negative) crossProduct means ast2 has smaller angle
        #  crossProduct = 0 means they are colinear. take shorter distance as 'lower' asteroid in ranking.

        orientation = AsteroidScanner.crossProduct(ast1, ast2, cls.__asteroid0)

        if orientation == 0:
            # will return 0 if asts 1 and 2 are the same
            return AsteroidScanner.squareDistance(ast1, cls.__asteroid0) - AsteroidScanner.squareDistance(ast2, cls.__asteroid0)

        return -orientation

    # return the cosine of angle ast1 -> ast2 -> ast3
    @staticmethod
    def cosine(ast1, ast2, ast3):
        # dot product of rays 1-2, 3-2
        dotProduct = (ast1[0] - ast2[0])*(ast3[0] - ast2[0]) + \
               (ast1[1] - ast2[1])*(ast3[1] - ast2[1])
        squareDistance12 = AsteroidScanner.squareDistance(ast1, ast2)
        squareDistance32 = AsteroidScanner.squareDistance(ast3, ast2)

        # Return Cosine value: dot Product divided by the product of the lengths
        return dotProduct / math.sqrt(squareDistance12*squareDistance32)

    @staticmethod
    def importAsteroids(inputFile):

        astList = list()
        numAsts = 0
        try:
            with open(inputFile, 'r') as inputHandle:
                numAsts = int(inputHandle.readline())

                # For all lines in inputHandle, append a coordinate tuple
                astList = [(int(coordPair[0]),int(coordPair[1])) for coordPair in [line.split() for line in inputHandle]]
                
        except Exception as err:
            print(err)


        try:
            assert numAsts == len(astList)
        except AssertionError:
            if numAsts < len(astList):
                print('Asteroid number mismatch. More asteroids than expected')
                # raise ValueError
            else:
                print('Asteroid number mismatch. Fewer asteroids supplied than expected.')
                # raise ValueError

        # TODO: Check if input is as expected:
        # Non-zero asts?
        # numAsts matches actual number of asts provided?

        return astList

    # Main method to scan asteroid list and find 'best' viewing asteroid (minimum viewing angle).
    @staticmethod
    def scan(astList):
        pass
