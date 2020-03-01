import unittest
from stock_prices import stock_prices


class TestStockPrices(unittest.TestCase):
    def test_picks_best_days(self):
        """
        Test that best buying and selling days are picked.
        """
        self.assertEqual(stock_prices([17, 3, 6, 9, 15, 8, 6, 1, 10]), [1, 4])

    def test_picks_best_days_when_last_day_is_lowest(self):
        """
        Test that best buying and selling days are picked when the lowest day is the last day.
        """
        self.assertEqual(stock_prices([3, 8, 6, 9, 15, 17, 6, 10, 1]), [0, 5])

    def test_picks_best_days_when_first_day_is_highest(self):
        """
        Test that best buying and selling days are picked when the highest day is the first day.
        """
        self.assertEqual(stock_prices([17, 3, 6, 9, 10, 8, 6, 4, 15]), [1, 8])


if __name__ == "__main__":
    unittest.main()
