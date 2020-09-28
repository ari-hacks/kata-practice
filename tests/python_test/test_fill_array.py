  
import unittest
from katas.python.kyu8.fill_array import fill_array

class TestFillArray(unittest.TestCase): 
    def test_array(self):
        self.assertEqual(fill_array(4), [0,1,2,3])
        self.assertEqual(fill_array(0), [])
        self.assertEqual(fill_array(), [])

