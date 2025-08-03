
import unittest
from simple_calculator import SimpleCalculator

def SimpleCalculator():
    pass
class Test(unittest.TestCase):

    def test_addition(self):
        # self.assertEqual(SimpleCalculator.add(self, 5,5), 10)
        self.assertEqual(self.calc.add(5,5), 10)

    def test_subtraction(self):
        # self.assertEqual(SimpleCalculator.subtract(self, 10,5), 5)
        self.assertEqual(self.calc.subtract(5,5), 0)

    def test_multiplication(self):
        # self.assertEqual(SimpleCalculator.multiply(self, 10,5), 50)
        self.assertEqual(self.calc.multiply(5,5), 25)

    def test_division(self):
        # self.assertEqual(SimpleCalculator.divide(self, 20,5), 4)
        self.assertEqual(self.calc.divide(5,5), 1)
        self.assertEqual(self.calc.divide(5,0), ZeroDivisionError())
        # self.assertEqual(SimpleCalculator.divide(self, 20,0), ZeroDivisionError())