import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
   
    def setUp(self):
        
        # Initialize a new calculator object for each test
        self.calc = SimpleCalculator()

    def test_addition(self):
        
        # Test positive numbers
        self.assertEqual(self.calc.add(5, 7), 12)
        # Test negative numbers
        self.assertEqual(self.calc.add(-5, -7), -12)
        # Test mix of positive and negative
        self.assertEqual(self.calc.add(10, -5), 5)
        # Test adding zero
        self.assertEqual(self.calc.add(0, 8), 8)

    def test_subtraction(self):
        
        # Test positive result
        self.assertEqual(self.calc.subtract(10, 4), 6)
        # Test negative result
        self.assertEqual(self.calc.subtract(4, 10), -6)
        # Test with negative numbers
        self.assertEqual(self.calc.subtract(5, -5), 10)
        # Test subtracting zero
        self.assertEqual(self.calc.subtract(15, 0), 15)

    def test_multiplication(self):
       
        # Test positive multiplication
        self.assertEqual(self.calc.multiply(3, 8), 24)
        # Test multiplication with zero
        self.assertEqual(self.calc.multiply(50, 0), 0)
        # Test multiplication with negative numbers
        self.assertEqual(self.calc.multiply(-2, 6), -12)
        self.assertEqual(self.calc.multiply(-5, -5), 25)

    def test_division(self):
        
        # Test normal division (float result)
        self.assertEqual(self.calc.divide(10, 5), 2.0)
        # Test division resulting in a decimal
        self.assertEqual(self.calc.divide(10, 4), 2.5)
        # Test division by zero (should return None as per the SimpleCalculator class)
        self.assertIsNone(self.calc.divide(10, 0))