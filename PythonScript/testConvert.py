# This Python file uses the following encoding: utf-8

# Use command line to do unit test.
# - Go to folder "PythonScript\"
# - Run "python -m unittest discover ."

import unittest
import Convert
from Convert import CheckedToneMarker


class TestConvert(unittest.TestCase):
    def test_convert(self):
        self.assertEqual(u"‘", Convert.Convert(u"『"))
        self.assertEqual("b", Convert.Convert("b~b~"))

    def test_remove_redundant_subscript(self):
        self.assertEqual("", Convert.remove_redundant_subscript_signs(""))

        self.assertEqual("b~", Convert.remove_redundant_subscript_signs("b~"))
        self.assertEqual(
            "abc", Convert.remove_redundant_subscript_signs("ab~b~c"))
        self.assertEqual(u"舍", Convert.Convert(u"舍~舍~"))

    def test_add_superscript(self):
        self.assertEqual("", CheckedToneMarker("").mark())
        self.assertEqual(
            u"^入^", Convert.mark_checked_tone_chars(u"入"))
        self.assertEqual(
            u"^入^^日^", Convert.mark_checked_tone_chars(u"入日"))
        self.assertEqual(
            u"江^入^^日^", Convert.mark_checked_tone_chars(u"江入日"))
        self.assertEqual(
            u"江~屋~^日^", Convert.mark_checked_tone_chars(
                u"江~屋~日"),
            "do not mark checked tone if char is an alternative word")


if __name__ == '__main__':
    unittest.main()
