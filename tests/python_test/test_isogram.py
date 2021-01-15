
  
import unittest
from katas.python.kyu7.isogram import is_isogram

class TestIs_Isogram(unittest.TestCase): 
    def test_array(self):
        self.assertEqual(is_isogram("Dermatoglyphics"), True )
        self.assertEqual(is_isogram("isogram"), True )
        self.assertEqual(is_isogram("aba"), False, "same chars may not be adjacent" )
        self.assertEqual(is_isogram("moOse"), False, "same chars may not be same case" )
        self.assertEqual(is_isogram("isIsogram"), False )
        self.assertEqual(is_isogram(""), True, "an empty string is a valid isogram" )
        
