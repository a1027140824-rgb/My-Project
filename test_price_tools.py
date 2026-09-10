import unittest

from price_tools import calculate_tax
from price_tools import final_price
from price_tools import most_expensive
from price_tools import split_bill


class PriceToolsTests(unittest.TestCase):
    def test_final_price_applies_discount(self) -> None:
        self.assertEqual(final_price(100.0, 20.0), 80.0)

    def test_final_price_accepts_no_discount(self) -> None:
        self.assertEqual(final_price(49.99, 0.0), 49.99)

    def test_split_bill_divides_total(self) -> None:
        self.assertEqual(split_bill(120.0, 4), 30.0)

    def test_split_bill_rounds_result(self) -> None:
        self.assertEqual(split_bill(100.0, 3), 33.33)

    def test_calculate_tax(self) -> None:
        self.assertEqual(calculate_tax(100.0, 8.0), 8.0)

    def test_most_expensive_returns_highest_value(self) -> None:
        self.assertEqual(most_expensive([12.5, 30.0, 8.0]), 30.0)

    def test_most_expensive_returns_none_for_empty_list(self) -> None:
        self.assertIsNone(most_expensive([]))


if __name__ == "__main__":
    unittest.main()
