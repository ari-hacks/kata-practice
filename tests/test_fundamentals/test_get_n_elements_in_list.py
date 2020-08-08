import unittest
from katas.fundamentals.get_n_elements_in_list import take


class FundamentalsTest(unittest.TestCase):
      def test_take(self):
         self.assertEqual(take([0, 1, 2, 3, 5, 8, 13], 3), [0, 1, 2], "should return the first 3 items")

    