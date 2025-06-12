import unittest
import math
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(2.5, 1.5), 1.0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 3), -3)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(1.5, 2), 3.0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(0, 5), 0)
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)

    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)
        self.assertEqual(self.calc.power(0, 5), 0)
        self.assertEqual(self.calc.power(2, -2), 0.25)
        self.assertEqual(self.calc.power(4, 0.5), 2)

    def test_sqrt(self):
        self.assertEqual(self.calc.sqrt(9), 3)
        self.assertEqual(self.calc.sqrt(0), 0)
        self.assertEqual(self.calc.sqrt(2), math.sqrt(2))
        with self.assertRaises(ValueError):
            self.calc.sqrt(-1)

    def test_log(self):
        self.assertEqual(self.calc.log(100), 2)
        self.assertEqual(self.calc.log(1), 0)
        self.assertEqual(self.calc.log(8, 2), 3)
        with self.assertRaises(ValueError):
            self.calc.log(0)
        with self.assertRaises(ValueError):
            self.calc.log(-1)
        with self.assertRaises(ValueError):
            self.calc.log(10, 0) # Base is 0
        with self.assertRaises(ValueError):
            self.calc.log(10, 1) # Base is 1
        with self.assertRaises(ValueError):
            self.calc.log(10, -2) # Base is negative

    def test_ln(self):
        self.assertEqual(self.calc.ln(math.e), 1)
        self.assertEqual(self.calc.ln(1), 0)
        self.assertAlmostEqual(self.calc.ln(10), math.log(10))
        with self.assertRaises(ValueError):
            self.calc.ln(0)
        with self.assertRaises(ValueError):
            self.calc.ln(-1)

    def test_sin(self):
        self.assertEqual(self.calc.sin(0), 0)
        self.assertEqual(self.calc.sin(math.pi / 2), 1)
        self.assertAlmostEqual(self.calc.sin(math.pi / 6), 0.5)

    def test_cos(self):
        self.assertEqual(self.calc.cos(0), 1)
        self.assertAlmostEqual(self.calc.cos(math.pi / 2), 0)
        self.assertAlmostEqual(self.calc.cos(math.pi / 3), 0.5)

    def test_tan(self):
        self.assertEqual(self.calc.tan(0), 0)
        self.assertAlmostEqual(self.calc.tan(math.pi / 4), 1)
        # Test for large value near pi/2 where tan approaches infinity
        # Value for tan(pi/2 - 1e-9) is around 999999856.027
        self.assertTrue(self.calc.tan(math.pi/2 - 1e-9) > 1e8)
        self.assertTrue(self.calc.tan(math.pi/2 + 1e-9) < -1e8)


if __name__ == '__main__':
    unittest.main()
