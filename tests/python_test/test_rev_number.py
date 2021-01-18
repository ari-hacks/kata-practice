import unittest
from katas.python.kyu7.rev_number import reverse_number

class TestRevNumber(unittest.TestCase): 
    def test_rev_number(self):
        self.assertEqual(reverse_number(123), 321)
        self.assertEqual(reverse_number(-123), -321, 'Negative Numbers should be preserved')
        self.assertEqual(reverse_number(4321234), 4321234)
        self.assertEqual(reverse_number(5), 5)
        self.assertEqual(reverse_number(0), 0)
        self.assertEqual(reverse_number(98989898), 89898989)
