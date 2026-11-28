# test_calculator.py
import unittest
from calculator import (
    addition,
    subtraction,
    multiplication,
    division,
    exponentiation,
    extracting,
    factorial,
)

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(5, 3), 8)
        self.assertEqual(addition(-2, 2), 0)

    def test_subtraction(self):
        self.assertEqual(subtraction(10, 4), 6)
        self.assertEqual(subtraction(3, 5), -2)

    def test_multiplication(self):
        self.assertEqual(multiplication(3, 4), 12)
        self.assertEqual(multiplication(5, 0), 0)

    def test_division(self):
        # Позитивный сценарий
        self.assertEqual(division(10, 2), 5.0)
        # Негативный сценарий
        self.assertEqual(division(10, 0), 10)

    def test_exponentiation(self):
        self.assertEqual(exponentiation(2, 3), 8)
        self.assertEqual(exponentiation(5, 0), 1)

    def test_extracting(self):
        self.assertEqual(extracting(9), 3.0)
        self.assertEqual(extracting(0), 0.0)

    def test_factorial(self):
        self.assertEqual(factorial(5.0), 120.0)
        self.assertEqual(factorial(0.0), 1.0)
        # Проверка граничных условий
        self.assertEqual(factorial(-3.0), -3.0)  # Отрицательное возвращает само себя
        self.assertEqual(factorial(4.5), 4.5)    # Дробное возвращает само себя

if __name__ == "__main__":
    unittest.main()