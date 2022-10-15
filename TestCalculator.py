import unittest
from main import calculate


class TestCalculator(unittest.TestCase):
    def test_calculate_can_add_floats(self):
        answer = calculate(1.2, 4.5, '+')

        self.assertAlmostEqual(5.7, answer, 3)

    def test_calculate_can_subtract_floats(self):
        answer = calculate(1.2, 4.5, '-')

        self.assertAlmostEqual(-3.3, answer, 3)

    def test_calculate_can_multiply_floats(self):
        answer = calculate(1.2, 4.5, '*')

        self.assertAlmostEqual(5.4, answer, 3)

    def test_calculate_can_divide_floats(self):
        answer = calculate(3.0, 1.5, '/')

        self.assertAlmostEqual(2.0, answer, 3)

    def test_calculate_can_calculate_exponential(self):
        answer = calculate(3.0, 2, '**')
        self.assertAlmostEqual(9.0, answer, 3)

    def test_calculate_throws_error_for_unknown_operator(self):
        with self.assertRaises(ValueError):
            calculate(3.0, 2, 'p')

if __name__ == '__main__':
    unittest.main()
