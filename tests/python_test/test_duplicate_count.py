import unittest
from katas.python.kyu6.duplicate_count import duplicate_count
import pytest

class TestGetAverage(unittest.TestCase): 
    # @pytest.mark.usefixtures('do_twice')
    def test_duplicate_count(self):
        self.assertEqual(duplicate_count("abcde"), 0)
        self.assertEqual(duplicate_count("abcdea"), 1)
        self.assertEqual(duplicate_count("indivisibility"), 1)
        self.assertEqual(duplicate_count("aA11"), 2)
