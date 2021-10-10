# This Python file uses the following encoding: utf-8

# Use command line to do unit test.
# - Go to folder "PythonScript\"
# - Run "python -m unittest discover ."

import unittest
import Convert

class TestConvert(unittest.TestCase): 
    def test_convert(self):
        self.assertEqual(Convert.Convert(u"『"), u"‘")
    def test_remove_redundant_subscript(self):
        self.assertEqual("", Convert.remove_redundant_subscript(""))
        self.assertEqual("b", Convert.remove_redundant_subscript("b~b~"))
        self.assertEqual("b~", Convert.remove_redundant_subscript("b~"))
        self.assertEqual("abc", Convert.remove_redundant_subscript("ab~b~c"))
        self.assertEqual(u"舍", Convert.Convert(u"舍~舍~"))
    def test_add_superscript(self):
        self.assertEqual("", Convert.remove_redundant_subscript(""))

if __name__ == '__main__':
    unittest.main()
