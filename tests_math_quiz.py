import unittest
from math_quiz import function_O, function_M, function_G


class TestMathGame(unittest.TestCase):

    def test_function_O(self):
        # Test if random numbers generated are within the specified range
        MINIMUM_VALUE = 1
        MAXIMUM_VALUE = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_O(MINIMUM_VALUE, MAXIMUM_VALUE)
            self.assertTrue(MINIMUM_VALUE <= rand_num <= MAXIMUM_VALUE)

    def test_function_M(self):
        # Test if random arithmetic operators are one of the specified values
        valid_operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random values
            rand_operator = function_M()
            self.assertIn(rand_operator, valid_operators)

    def test_function_G(self):
        test_cases = [
            (5, 2, '+', 7),
            # Add more test cases here

            # Example:
            (3, 4, '*', 12),
        ]

        for num1, num2, operator, expected_result in test_cases:
            result = function_G(num1, num2, operator)
            self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
