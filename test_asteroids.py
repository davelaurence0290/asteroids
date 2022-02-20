"""Test Module for Asteroid Scanner Exercise."""

import unittest
import math
import asteroid_scanner

class TestAsteroids(unittest.TestCase):
    """Test class for housing testing methods."""

    def test_squared_distance_ints(self):
        """Test square_distance() function with simple integers."""
        expected = 2
        actual = asteroid_scanner.AsteroidScanner.squared_distance((1, 1), (0, 0))
        self.assertEqual(expected, actual, f'Squared distance should be {expected}')

    def test_squared_distance_ints2(self):
        """Test square_distance() function with simple integers."""
        expected = 25
        actual = asteroid_scanner.AsteroidScanner.squared_distance((2, 1), (-1, 5))
        self.assertEqual(expected, actual, f'Squared distance should be {expected}')

    def test_squared_distance_same(self):
        """Test square_distance() function with the same integer pairs."""
        expected = 0
        actual = asteroid_scanner.AsteroidScanner.squared_distance((1, 1), (1, 1),)
        self.assertEqual(expected, actual, f'Squared distance should be {expected}')

    def test_cross_product_90deg(self):
        """Test cross_product() at known 90deg vectors."""
        expected = 25
        actual = asteroid_scanner.AsteroidScanner.cross_product((5, 0), (0, 5), (0, 0))
        self.assertEqual(expected, actual, f'Squared distance should be {expected}')

    def test_cross_product_1(self):
        """Test cross_product() with arbitrary vectors."""
        expected = -174
        actual = asteroid_scanner.AsteroidScanner.cross_product((-8, 10), (15, 3), (0, 0))
        self.assertEqual(expected, actual, f'Squared distance should be {expected}')

    def test_cross_product_same(self):
        """Test cross_product() with 0-length vectors."""
        expected = 0
        actual = asteroid_scanner.AsteroidScanner.cross_product((0, 0), (0, 0), (0, 0))
        self.assertEqual(expected, actual, f'Squared distance should be {expected}')

    def test_cosine_0deg(self):
        """Test cosine() with known 0deg vectors."""
        expected = 1
        actual = asteroid_scanner.AsteroidScanner.cosine((2, 0), (0, 0), (4, 0))
        self.assertEqual(expected, actual, f'Squared distance should be {expected}')

    def test_cosine_90deg(self):
        """Test cosine() with known 90deg vectors."""
        expected = 0
        actual = asteroid_scanner.AsteroidScanner.cosine((5, 5), (0, 0), (5, -5))
        self.assertEqual(expected, actual, f'Squared distance should be {expected}')

    def test_cosine_180deg(self):
        """Test cosine() with known 180deg vectors."""
        expected = -1
        actual = asteroid_scanner.AsteroidScanner.cosine((-1, -1), (0, 0), (1, 1))
        self.assertEqual(expected, actual, f'Squared distance should be {expected}')

    def test_cosine_45deg(self):
        """Test cosine() with known 45deg vectors."""
        expected = math.cos(math.pi / 4)
        actual = asteroid_scanner.AsteroidScanner.cosine((1, 1), (0, 0), (1, 0))
        self.assertAlmostEqual(expected, actual, 7, f'Squared distance should be {expected}')

    def test_import_asteroids_input1(self):
        """Test import_asteroids(). Ensure a list of asteroids is retrieved correctly"""
        expected = [(0, 0), (1, 0), (1, 1), (0, 1), (3, 3)]
        actual = asteroid_scanner.AsteroidScanner.import_asteroids('input\\input1.txt')
        self.assertEqual(expected, actual, {'List should contain ': expected})

    def test_import_asteroids_input7(self):
        """Test import_asteroids(). Ensure a list of asteroids is retrieved correctly"""
        expected = []
        actual = asteroid_scanner.AsteroidScanner.import_asteroids('input\\input7.txt')
        self.assertEqual(expected, actual, {'List should contain ': expected})

    # The ValueError Exception that triggers in this test is commented out for 'release'
    def test_import_asteroids_input97(self):
        """Test import_asteroids(). Ensure a list of asteroids is retrieved correctly"""
        with self.assertRaises(ValueError,
                               msg='Should fail: supplied more asteroids than expected'):
            asteroid_scanner.AsteroidScanner.import_asteroids('input\\input97.txt')

    # The ValueError Exception that triggers in this test is commented out for 'release'
    def test_import_asteroids_input98(self):
        """Test import_asteroids(). Ensure a list of asteroids is retrieved correctly"""
        with self.assertRaises(ValueError,
                               msg='Should fail: supplied more asteroids than expected'):
            asteroid_scanner.AsteroidScanner.import_asteroids('input\\input98.txt')

    # The ValueError Exception that triggers in this test is commented out for 'release'
    def test_import_asteroids_input99(self):
        """Test import_asteroids(). Ensure a list of asteroids is retrieved correctly"""
        with self.assertRaises(ValueError,
                               msg='Should fail: supplied fewer asteroids than expected'):
            asteroid_scanner.AsteroidScanner.import_asteroids('input\\input99.txt')

    def test_scan_input1(self):
        """Test scan() with input1.txt"""
        ast_list = asteroid_scanner.AsteroidScanner.import_asteroids('input\\input1.txt')
        expected = (3, 3)
        actual = asteroid_scanner.AsteroidScanner.scan(ast_list)
        self.assertEqual(expected, actual, f'Best asteroid should be {expected}')

    def test_scan_input2(self):
        """Test scan() with input2.txt"""
        ast_list = asteroid_scanner.AsteroidScanner.import_asteroids('input\\input2.txt')
        expected = (0, 25)
        actual = asteroid_scanner.AsteroidScanner.scan(ast_list)
        self.assertEqual(expected, actual, f'Best asteroid should be {expected}')

    def test_scan_input3(self):
        """Test scan() with input3.txt"""
        ast_list = asteroid_scanner.AsteroidScanner.import_asteroids('input\\input3.txt')
        expected = (-8, -10)
        actual = asteroid_scanner.AsteroidScanner.scan(ast_list)
        self.assertEqual(expected, actual, f'Best asteroid should be {expected}')

    def test_scan_input4(self):
        """Test scan() with input4.txt"""
        ast_list = asteroid_scanner.AsteroidScanner.import_asteroids('input\\input4.txt')
        expected = (-15, 18)
        actual = asteroid_scanner.AsteroidScanner.scan(ast_list)
        self.assertEqual(expected, actual, f'Best asteroid should be {expected}')

    def test_scan_input5(self):
        """Test scan() with input5.txt"""
        ast_list = asteroid_scanner.AsteroidScanner.import_asteroids('input\\input5.txt')
        expected = (20, 24)
        actual = asteroid_scanner.AsteroidScanner.scan(ast_list)
        self.assertEqual(expected, actual, f'Best asteroid should be {expected}')

    def test_scan_input6(self):
        """Test scan() with input6.txt"""
        ast_list = asteroid_scanner.AsteroidScanner.import_asteroids('input\\input6.txt')
        expected = (-30, 0)
        actual = asteroid_scanner.AsteroidScanner.scan(ast_list)
        self.assertEqual(expected, actual, f'Best asteroid should be {expected}')

    def test_scan_input95(self):
        """Test scan() with input95.txt. File is empty"""
        ast_list = asteroid_scanner.AsteroidScanner.import_asteroids('input\\input95.txt')
        expected = None
        actual = asteroid_scanner.AsteroidScanner.scan(ast_list)
        self.assertEqual(expected, actual, f'Best asteroid should be {expected}')

    def test_scan_input96(self):
        """Test scan() with input96.txt. File contains only two points. Trivial Solution"""
        ast_list = asteroid_scanner.AsteroidScanner.import_asteroids('input\\input96.txt')
        expected = (1, 0)
        actual = asteroid_scanner.AsteroidScanner.scan(ast_list)
        self.assertEqual(expected, actual, f'Best asteroid should be {expected}')

    def test_scan_input97(self):
        """Test scan() with input97.txt. File contains no points"""
        ast_list = asteroid_scanner.AsteroidScanner.import_asteroids('input\\input97.txt')
        expected = None
        actual = asteroid_scanner.AsteroidScanner.scan(ast_list)
        self.assertEqual(expected, actual, f'Best asteroid should be {expected}')

    def test_scan_input98(self):
        """Test scan() with input98.txt. Mismatched: asteroids declared < supplied."""
        ast_list = asteroid_scanner.AsteroidScanner.import_asteroids('input\\input98.txt')
        expected = (3, 3)
        actual = asteroid_scanner.AsteroidScanner.scan(ast_list)
        self.assertEqual(expected, actual, f'Best asteroid should be {expected}')

    def test_scan_input99(self):
        """Test scan() with input99.txt. Mismatched: asteroids declared > supplied."""
        ast_list = asteroid_scanner.AsteroidScanner.import_asteroids('input\\input99.txt')
        expected = (3, 3)
        actual = asteroid_scanner.AsteroidScanner.scan(ast_list)
        self.assertEqual(expected, actual, f'Best asteroid should be {expected}')


if __name__ == '__main__':
    unittest.main()
