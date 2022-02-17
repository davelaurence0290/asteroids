# Class to house the asteroid scanning methods

import math
from functools import cmp_to_key

class AsteroidScanner:
    # Variable to store lowest-Y asteroid location
    __asteroid0 = tuple()

    # Setting __asteroid0
    @classmethod
    def set_asteroid0(cls, asteroid0):
        cls.__asteroid0 = asteroid0

    # function to calculate distance between two Asteroids
    # (square of distance will be sufficient for comparisons)
    @staticmethod
    def square_distance(ast1, ast2):
        return (ast1[1]-ast2[1])**2 + (ast1[0]-ast2[0])**2

    # function to calculate Cross-Product
    # used to check orientation during algorithm progression, and to sort initial asteroid points by angle.
    @staticmethod
    def cross_product(ast1, ast2, ast3):
        return (ast1[0] - ast3[0]) * (ast2[1] - ast3[1]) - \
               (ast1[1] - ast3[1]) * (ast2[0] - ast3[0])

    # function for initial sort of asteroids according to their angle with asteroid0
    @classmethod
    def angle_sort(cls, ast1, ast2):
        # using cross product to tell difference in angle
        # 'clockwise' (positive) cross_product means ast2 has larger angle with x-axis
        # 'counter-clockwise' (negative) cross_product means ast2 has smaller angle
        #  cross_product = 0 means they are colinear. take shorter distance as 'lower' asteroid in ranking.

        orientation = AsteroidScanner.cross_product(ast1, ast2, cls.__asteroid0)

        if orientation == 0:
            # will return 0 if asts 1 and 2 are the same
            return AsteroidScanner.square_distance(ast1, cls.__asteroid0) - AsteroidScanner.square_distance(ast2, cls.__asteroid0)

        return -orientation

    # return the cosine of angle ast1 -> ast2 -> ast3
    @staticmethod
    def cosine(ast1, ast2, ast3):
        # dot product of rays 1-2, 3-2
        dotProduct = (ast1[0] - ast2[0])*(ast3[0] - ast2[0]) + \
               (ast1[1] - ast2[1])*(ast3[1] - ast2[1])
        square_distance12 = AsteroidScanner.square_distance(ast1, ast2)
        square_distance32 = AsteroidScanner.square_distance(ast3, ast2)

        # Return Cosine value: dot Product divided by the product of the lengths
        return dotProduct / math.sqrt(square_distance12*square_distance32)

    @staticmethod
    def import_asteroids(inputFile):

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

        return astList

    @staticmethod
    def initial_xy_sort(ast1, ast2):
        if ast1[1] == ast2[1]:
            return ast1[0] - ast2[0]
        else:
            return ast1[1] - ast2[1]

    @staticmethod
    def graham_scan(astList):
        # Sort asteroids by lowest 'y' coordinate first, then lowest 'x'
        astList = sorted(astList,key=cmp_to_key(AsteroidScanner.initial_xy_sort))
        # Remove and save __asteroid0 (first entry)
        AsteroidScanner.set_asteroid0(astList.pop(0))
        # Sort asteroids by polar angle with __asteroid0 and x-axis
        astList = sorted(astList,key=cmp_to_key(AsteroidScanner.angle_sort))

        # Construct convex hull
        convHull = list()
        # Add first two points (after sorting, __asteroid0 and first sorted point are guaranteed to be in the hull)
        convHull.append(AsteroidScanner.__asteroid0)
        convHull.append(astList.pop(0))
        for asteroid in astList:
            # Ensure there are at least 2 points in convHull and that the to-be-added point results in a 'left' turn.
            # If 'right turn' then pop off the last point in convHull, it's internal.
            while len(convHull) > 1 and \
                  AsteroidScanner.cross_product(asteroid, convHull[len(convHull)-2], convHull[len(convHull)-1]) < -1 :
                convHull.pop()
            convHull.append(asteroid)

        return convHull

    @staticmethod
    def get_best_asteroid(convHull):
        # Iterate through convex hull, find minimum viewing angle
        # Since angle will be < 180deg, using cosine to rank will suffice.
        # Maximum Cosine -> Smallest angle
        tempCosine = -1
        bigCosine = -1
        bestAstNum = -1
        for astNum in range(len(convHull)-1):
            tempCosine = AsteroidScanner.cosine(convHull[astNum-1], convHull[astNum], convHull[astNum+1])
            #print(str(convHull[astNum]), 'cosine=', tempCosine)
            if tempCosine > bigCosine:
                bigCosine = tempCosine
                bestAstNum = astNum

        # Compute last asteroid (loops to beginning of list)
        tempCosine = AsteroidScanner.cosine(convHull[len(convHull)-2], convHull[len(convHull)-1], convHull[0])
        if tempCosine > bigCosine:
            bestAstNum = len(convHull) - 1

        return convHull[bestAstNum]


    # Main method to scan asteroid list and find 'best' viewing asteroid (minimum viewing angle).
    @staticmethod
    def scan(astList):
        # Remove duplicates
        astList = list(set(astList))

        # Get Convex hull (the outer ring of asteroids containing all others)
        convHull = AsteroidScanner.graham_scan(astList)
        # Choose the best asteroid based on viewing angle
        bestAsteroid = AsteroidScanner.get_best_asteroid(convHull)

        return bestAsteroid