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
        self.assertEqual("", CheckedToneMarker("").mark_book())
        self.assertEqual('<font class="checkedTone">入</font>',
                         CheckedToneMarker("入").mark_book())
        self.assertEqual('江<font class="checkedTone">入</font><font class="checkedTone">日</font>',
                         CheckedToneMarker("江入日").mark_book())
        self.assertEqual("江~屋~" + '<font class="checkedTone">日</font>', CheckedToneMarker("江~屋~日").mark_book(),
                         "do not mark checked tone if char is an alternative word")
        self.assertEqual("江~屋~" + '<font class="checkedTone">日</font>', CheckedToneMarker("江~屋~日").mark_book(),
                         "do not mark checked tone if char is an alternative word")


if __name__ == '__main__':
    unittest.main()
