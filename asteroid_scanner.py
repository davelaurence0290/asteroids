"""Module housing the AsteroidScanner utility class."""

import math
from functools import cmp_to_key


class AsteroidScanner:
    """AsteroidScanner utility class.

    The static methods herein provide the functionality to find the best-viewing-angle asteroid
    in a set of asteroids by returning its 2D coordinate position."""

    # Variable to store lowest-Y asteroid location
    __asteroid0 = tuple()

    @classmethod
    def set_asteroid0(cls, asteroid0):
        """Set class variable __asteroid0"""
        cls.__asteroid0 = asteroid0

    @staticmethod
    def squared_distance(ast1, ast2):
        """Return the square of the distance between two asteroids"""
        # (square of distance will be sufficient for comparisons)
        return (ast1[1]-ast2[1])**2 + (ast1[0]-ast2[0])**2

    @staticmethod
    def cross_product(ast1, ast2, ast3):
        """Calculate the cross product of vector rays: (ast1-ast3) X (ast2-ast3)"""
        # Used to check orientation during algorithm progression, and to sort initial asteroid
        # points by angle.
        return (ast1[0] - ast3[0]) * (ast2[1] - ast3[1]) - \
               (ast1[1] - ast3[1]) * (ast2[0] - ast3[0])

    # function for initial sort of asteroids according to their angle with asteroid0
    @classmethod
    def angle_sort(cls, ast1, ast2):
        """Calculate the orientation of two points w.r.t. the angle they form with
        ___asteroid and the x-axis"""
        # using cross product to tell difference in angle
        # 'clockwise' (positive) cross_product means ast2 has larger angle with x-axis
        # 'counter-clockwise' (negative) cross_product means ast2 has smaller angle
        #  cross_product = 0 means they are collinear. take shorter distance as 'lower'
        #  asteroid in ranking.
        orientation = AsteroidScanner.cross_product(ast1, ast2, cls.__asteroid0)
        # if asts 1 and 2 are on the same line
        if orientation == 0:
            # return comparison of distances
            return AsteroidScanner.squared_distance(ast1, cls.__asteroid0) - \
                   AsteroidScanner.squared_distance(ast2, cls.__asteroid0)
        return -orientation

    # return the cosine of angle ast1 -> ast2 -> ast3
    @staticmethod
    def cosine(ast1, ast2, ast3):
        """# Calculate and return the cosine of angle ast1 -> ast2 -> ast3"""
        # dot product of rays 1-2, 3-2
        dot_product = (ast1[0] - ast2[0])*(ast3[0] - ast2[0]) + \
                      (ast1[1] - ast2[1])*(ast3[1] - ast2[1])
        squared_distance12 = AsteroidScanner.squared_distance(ast1, ast2)
        squared_distance32 = AsteroidScanner.squared_distance(ast3, ast2)

        # Return Cosine value: dot Product divided by the product of the lengths
        return dot_product / math.sqrt(squared_distance12*squared_distance32)

    @staticmethod
    def import_asteroids(input_file):
        """Import the list of asteroid positions from file. Return the list."""
        ast_list = []
        num_asts = 0
        # Open file and read in the contents as coordinate tuples
        try:
            with open(input_file, 'r') as input_handle:
                num_asts = int(input_handle.readline())

                # For all lines in input_handle, append a coordinate tuple
                ast_list = [(int(coordPair[0]), int(coordPair[1])) for coordPair in
                            [line.split() for line in input_handle]]
        except FileNotFoundError as err:
            print(err)
        except ValueError as val_err:
            print("Invalid integer for asteroid count")
            print(val_err)
        # Check that number of asteroids declared is equal to actual number of tuples supplied.
        try:
            assert num_asts == len(ast_list)
        except AssertionError:
            if num_asts < len(ast_list):
                print('Asteroid number mismatch. More asteroids than expected')
                # raise ValueError
            else:
                print('Asteroid number mismatch. Fewer asteroids supplied than expected.')
                # raise ValueError

        return ast_list

    @staticmethod
    def initial_xy_sort(ast1, ast2):
        """Compare two asteroids by position. Return comparison of y coordinates, or x if same y."""
        if ast1[1] == ast2[1]:
            return ast1[0] - ast2[0]
        return ast1[1] - ast2[1]

    @staticmethod
    def graham_scan(ast_list):
        """Apply Graham's Scan algorithm to set of asteroids. Return convex hull list."""
        # Sort asteroids by lowest 'y' coordinate first, then lowest 'x'
        ast_list = sorted(ast_list, key=cmp_to_key(AsteroidScanner.initial_xy_sort))
        # Remove and save __asteroid0 (first entry)
        AsteroidScanner.set_asteroid0(ast_list.pop(0))
        # Sort asteroids by polar angle with __asteroid0 and x-axis
        ast_list = sorted(ast_list, key=cmp_to_key(AsteroidScanner.angle_sort))

        # Construct convex hull
        # Add first two points (after sorting, __asteroid0 and first sorted point are guaranteed to
        # be in the hull)
        conv_hull = [AsteroidScanner.__asteroid0, ast_list.pop(0)]
        for asteroid in ast_list:
            # Ensure there are at least 2 points in conv_hull and that the to-be-added point results
            # in a 'left' turn.
            # If 'right turn' then pop off the last point in conv_hull, it's internal.
            while len(conv_hull) > 1 and \
                  AsteroidScanner.cross_product(asteroid, conv_hull[len(conv_hull)-2],
                                                conv_hull[len(conv_hull)-1]) < 0:
                conv_hull.pop()
            conv_hull.append(asteroid)

        return conv_hull

    @staticmethod
    def get_best_asteroid(conv_hull):
        """Given a convex hull of asteroids, return """
        # Iterate through convex hull, find minimum viewing angle
        # Since angle will be < 180deg, using cosine to rank will suffice.
        # Maximum Cosine -> Smallest angle
        big_cosine = -1
        best_ast_num = 0
        for ast_num in range(len(conv_hull)-1):
            temp_cosine = AsteroidScanner.cosine(conv_hull[ast_num-1], conv_hull[ast_num],
                                                 conv_hull[ast_num+1])
            if temp_cosine > big_cosine:
                big_cosine = temp_cosine
                best_ast_num = ast_num

        # Compute last asteroid (loops to beginning of list)
        temp_cosine = AsteroidScanner.cosine(conv_hull[len(conv_hull)-2],
                                             conv_hull[len(conv_hull)-1], conv_hull[0])
        if temp_cosine > big_cosine:
            best_ast_num = len(conv_hull) - 1

        return conv_hull[best_ast_num]

    @staticmethod
    def scan(ast_list):
        """Main method to scan the list of asteroids. Return the best viewing angle asteroid."""
        # Remove duplicates
        ast_list = list(set(ast_list))

        # Check contents of list for trivial solutions
        if len(ast_list) == 0:
            print('No asteroids supplied.')
            return None
        if len(ast_list) < 3:
            # Trivial Solution: any asteroid in set will work
            return ast_list[0]

        # Get Convex hull (the outer ring of asteroids containing all others)
        conv_hull = AsteroidScanner.graham_scan(ast_list)
        # Choose the best asteroid based on viewing angle
        best_asteroid = AsteroidScanner.get_best_asteroid(conv_hull)

        return best_asteroid
