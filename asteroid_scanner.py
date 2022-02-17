# Class to house the asteroid scanning methods

import math


class AsteroidScanner:
    # Variable to store lowest-Y asteroid location
    __ast0 = tuple()

    # Setting __ast0
    @classmethod
    def setAst0(cls, ast0):
        cls.__ast0 = ast0

    # function to calculate distance between two Asteroids
    # (square of distance will be sufficient for comparisons)
    @staticmethod
    def squareD(ast1, ast2):
        return (ast1[1]-ast2[1])**2 + (ast1[0]-ast2[0])**2

    # function to calculate Cross-Product (cp)
    # used to check orientation during algorithm progression, and to sort initial asteroid points by angle.
    @staticmethod
    def cp(ast1, ast2, ast3):
        return (ast1[0] - ast3[0]) * (ast2[1] - ast3[1]) - \
                (ast1[1] - ast3[1])*(ast2[0] - ast3[0])

    # function for initial sort of asteroids according to their angle with ast0
    # will be used with qsort() (must have signature: int cmp(const void *a, const void *b))
    @classmethod
    def angleSort(cls, ast1, ast2):
        # using cross product to tell difference in angle
        # 'clockwise' (positive) cp means ast2 has larger angle with x-axis
        # 'counter-clockwise' (negative) cp means ast2 has smaller angle
        #  cp = 0 means they are colinear. take shorter distance as 'lower' asteroid in ranking.

        orientation = AsteroidScanner.cp(ast1, ast2, cls.__ast0)

        if orientation == 0:
            # will return 0 if asts 1 and 2 are the same
            return AsteroidScanner.squareD(ast1, cls.__ast0) - AsteroidScanner.squareD(ast2, cls.__ast0)

        return -orientation

    # return the cosine of angle ast1 -> ast2 -> ast3
    @staticmethod
    def getCos(ast1, ast2, ast3):
        # dot product of rays 1-2, 3-2
        dotP = (ast1[0] - ast2[0])*(ast3[0] - ast2[0]) + \
               (ast1[1] - ast2[1])*(ast3[1] - ast2[1])
        squareD12 = AsteroidScanner.squareD(ast1, ast2)
        squareD32 = AsteroidScanner.squareD(ast3, ast2)

        return dotP/math.sqrt(squareD12*squareD32)

    @staticmethod
    def importAsts(inputFile):

        with open(inputFile, 'r') as inputHandle:
            inputLines = inputHandle.readlines()

        # Read number of asteroids
        numAsts = int(inputLines.pop(0))

        astList = [(int(pair[0]), int(pair[1])) for pair in [line.split() for line in inputLines]]

        # TODO: Check if input is as expected:
        # Non-zero asts?
        # numAsts matches actual number of asts provided?

        return astList

    # Main method to scan asteroid list and find 'best' viewing asteroid (minimum viewing angle).
    @staticmethod
    def scan(astList):
        pass
