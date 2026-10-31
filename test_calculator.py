import unittest

from calculator import add, mean, multiply, subtract


class CalculatorTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)

    def test_mean(self):
        self.assertEqual(mean([1, 2, 3, 4]), 2.5)


if __name__ == '__main__':
    unittest.main()
