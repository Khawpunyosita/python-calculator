import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(-1, 2), 1)
        self.assertEqual(self.calc.add(-5, -2), -7)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(-5, -2), -3)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, -5), -10)
        self.assertEqual(self.calc.multiply(-7, -8), 56)

    def test_divide(self):
        self.assertEqual(self.calc.divide(8, -2), -4)
        self.assertEqual(self.calc.divide(-8, -2), 4)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(-7, 5), 3)
        self.assertEqual(self.calc.modulo(7, -5), -3)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()