import unittest
from main import calculate


class TestCalculator(unittest.TestCase):
    def test_calculate_can_add_floats(self):
        (success, answer) = calculate(1.2, 4.5, '+')

        self.assertEqual(True, success)
        self.assertAlmostEqual(5.7, answer, 3)

    def test_calculate_can_subtract_floats(self):
        (success, answer) = calculate(1.2, 4.5, '-')

        self.assertEqual(True, success)
        self.assertAlmostEqual(-3.3, answer, 3)

    def test_calculate_can_multiply_floats(self):
        (success, answer) = calculate(1.2, 4.5, '*')

        self.assertEqual(True, success)
        self.assertAlmostEqual(5.4, answer, 3)

    def test_calculate_can_divide_floats(self):
        (success, answer) = calculate(3.0, 1.5, '/')

        self.assertEqual(True, success)
        self.assertAlmostEqual(2.0, answer, 3)

    def test_calculate_can_calculate_exponential(self):
        (success, answer) = calculate(3.0, 2, '**')

        self.assertEqual(True, success)
        self.assertAlmostEqual(9.0, answer, 3)

    def test_calculate_returns_failure_for_unknown_operator(self):
        (success, answer) = calculate(3.0, 2, 'p')
        self.assertEqual(False, success)

if __name__ == '__main__':
    unittest.main()
