# This Python file uses the following encoding: utf-8

# Somehow, running this unit test in VS2015 is very slow (6 seconds).
# It is much faster to use command line to do unit test.
# How?
# - Go to folder "PythonScript\Dujing\"
# - Run "python -m unittest discover ."

import unittest
import Convert

class TestConvert(unittest.TestCase):
    def test_convert(self):
        self.assertEquals(Convert.Convert(u"『"), u"‘")
    def test_remove_redundant_subscript(self):
        self.assertEquals(Convert.remove_redundant_subscript(u"舍~舍~"), u"舍")

if __name__ == '__main__':
    unittest.main()
