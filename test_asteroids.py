import unittest
import asteroid_scanner
import math

class TestAsteroids(unittest.TestCase):

    def test_square_distance_ints(self):
        self.assertEqual(2, asteroid_scanner.AsteroidScanner.squareDistance((1,1), (0,0)), 'Squared distance should be 2')

    def test_square_distance_ints2(self):
        self.assertEqual(25, asteroid_scanner.AsteroidScanner.squareDistance((2,1), (-1,5)), 'Squared distance should be 25')

    def test_square_distance_same(self):
        self.assertEqual(0, asteroid_scanner.AsteroidScanner.squareDistance((1,1), (1,1),), 'Squared distance should be 0')

    def test_cross_product_90deg(self):
        self.assertEqual(25, asteroid_scanner.AsteroidScanner.crossProduct((5,0), (0,5), (0,0)), 'Cross Product should be 25')

    def test_cross_product_1(self):
        self.assertEqual(-174, asteroid_scanner.AsteroidScanner.crossProduct((-8,10), (15,3), (0,0)), 'Cross Product should be -174')

    def test_cross_product_same(self):
        self.assertEqual(0, asteroid_scanner.AsteroidScanner.crossProduct((0,0), (0,0), (0,0)), 'Cross Product should be 0')

    def test_cosine_0deg(self):
        self.assertEqual(1, asteroid_scanner.AsteroidScanner.cosine((2,0), (0,0), (4,0)), 'Cosine should be 1')

    def test_cosine_90deg(self):
        self.assertEqual(0, asteroid_scanner.AsteroidScanner.cosine((5,5), (0,0), (5,-5)), 'Cosine should be 0')

    def test_cosine_180deg(self):
        self.assertEqual(-1, asteroid_scanner.AsteroidScanner.cosine((-1,-1), (0,0), (1,1)), 'Cosine should be -1')

    def test_cosine_45deg(self):
        self.assertAlmostEqual(math.cos(math.pi / 4), asteroid_scanner.AsteroidScanner.cosine((1,1), (0,0), (1,0)), 7, 'Cosine should be .707')

    def test_import_asteroids_input1(self):
        expected = [(0,0),(1,0),(1,1),(0,1),(3,3)]
        actual = asteroid_scanner.AsteroidScanner.importAsteroids('input\input1.txt')
        self.assertEqual(expected, actual, {'List should contain ': expected})

    def test_import_asteroids_input98(self):
        with self.assertRaises(ValueError,msg='Should fail: supplied more asteroids than expected'):
            asteroid_scanner.AsteroidScanner.importAsteroids('input\input98.txt')

    def test_import_asteroids_input99(self):
        with self.assertRaises(ValueError,msg='Should fail: supplied fewer asteroids than expected'):
            asteroid_scanner.AsteroidScanner.importAsteroids('input\input99.txt')

if __name__ == '__main__':
    unittest.main()