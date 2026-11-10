import unittest


def add(first_number, second_number):
    return first_number + second_number


def subtract(first_number, second_number):
    return first_number - second_number


def divide(dividend, divisor):
    if divisor == 0:
        raise ValueError("Divisor cannot be zero")
    return dividend / divisor


class CalculatorTests(unittest.TestCase):
    def test_add_returns_sum(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract_returns_difference(self):
        self.fail("TODO: add an assertion for subtract")

    def test_divide_returns_quotient(self):
        self.fail("TODO: add an assertion for divide")

    def test_divide_by_zero_raises_value_error(self):
        self.fail("TODO: assert that divide raises ValueError")


if __name__ == "__main__":
    unittest.main()
