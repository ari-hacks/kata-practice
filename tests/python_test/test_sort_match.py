import unittest
from katas.python.kyu6.sort_match import scramble

class TestGetAverage(unittest.TestCase): 
    def test_average(self):
        self.assertEqual(scramble('rkqodlw', 'world'),  True)
        self.assertEqual(scramble('cedewaraaossoqqyt', 'codewars'), True)
        self.assertEqual(scramble('katas', 'steak'), False)
        self.assertEqual(scramble('scriptjava', 'javascript'), True)
        self.assertEqual(scramble('scriptingjava', 'javascript'), True)
