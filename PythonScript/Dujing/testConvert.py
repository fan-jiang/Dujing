# This Python file uses the following encoding: utf-8

# Somehow, running this unit test in VS2015 is very slow (6 seconds).
# It is much faster to use command line "python -m unittest discover ." to do unit test 
import unittest
import Convert

class TestConvert(unittest.TestCase):
    def test_Convert(self):
        self.assertEquals(Convert.Convert(u"『"), u"‘");

if __name__ == '__main__':
    unittest.main()
