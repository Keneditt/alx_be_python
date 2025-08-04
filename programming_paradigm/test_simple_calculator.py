# test_simple_calculator.py
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Create a calculator instance before each test"""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test addition operation with various inputs"""
        self.assertEqual(self.calc.add(2, 3), 5)        # Positive numbers
        self.assertEqual(self.calc.add(-1, 1), 0)        # Negative and positive
        self.assertEqual(self.calc.add(-5, -3), -8)      # Negative numbers
        self.assertEqual(self.calc.add(0, 7), 7)         # Zero identity
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)   # Decimals
        self.assertEqual(self.calc.add(1_000_000, 2_000_000), 3_000_000)  # Large numbers

    def test_subtraction(self):
        """Test subtraction operation with various inputs"""
        self.assertEqual(self.calc.subtract(5, 3), 2)      # Positive numbers
        self.assertEqual(self.calc.subtract(3, 5), -2)      # Reversed order
        self.assertEqual(self.calc.subtract(-1, -1), 0)     # Negative numbers
        self.assertEqual(self.calc.subtract(0, 5), -5)      # From zero
        self.assertEqual(self.calc.subtract(5, 0), 5)       # Subtract zero
        self.assertEqual(self.calc.subtract(2.5, 1.5), 1.0) # Decimals

    def test_multiplication(self):
        """Test multiplication operation with various inputs"""
        self.assertEqual(self.calc.multiply(3, 4), 12)       # Positive numbers
        self.assertEqual(self.calc.multiply(-3, 4), -12)     # Negative and positive
        self.assertEqual(self.calc.multiply(-3, -4), 12)     # Negative numbers
        self.assertEqual(self.calc.multiply(5, 0), 0)        # Zero multiplication
        self.assertEqual(self.calc.multiply(0, 5), 0)        # Zero multiplication
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)   # Decimals

    def test_division(self):
        """Test division operation with valid inputs"""
        self.assertEqual(self.calc.divide(10, 2), 5)         # Integer division
        self.assertEqual(self.calc.divide(9, 4), 2.25)       # Fraction result
        self.assertEqual(self.calc.divide(-10, 2), -5)       # Negative numerator
        self.assertEqual(self.calc.divide(10, -2), -5)       # Negative denominator
        self.assertEqual(self.calc.divide(-10, -2), 5)       # Negative both
        self.assertEqual(self.calc.divide(0, 5), 0)          # Zero numerator
        self.assertEqual(self.calc.divide(5.5, 2), 2.75)     # Decimals

    def test_division_by_zero(self):
        """Test division by zero returns None"""
        self.assertIsNone(self.calc.divide(10, 0))    # Positive numerator
        self.assertIsNone(self.calc.divide(-10, 0))   # Negative numerator
        self.assertIsNone(self.calc.divide(0, 0))      # Zero division (undefined)

if __name__ == '__main__':
    unittest.main()