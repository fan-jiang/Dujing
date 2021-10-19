# This Python file uses the following encoding: utf-8

from CheckedToneChars import checkedToneChars

charAfterOpenCcConversion_to_CharShownInSimplifiedText = {
    # Conversion for the quotation marks.
    u"「": u"“",
    u"」": u"”",
    u"『": u"‘",
    u"』": u"’",
    # OpenCC successfully converts the following characters to the simplified UTF-8 code.
    # However, these simplified characters could not be shown in most of Chinese Font families.
    # Thus, use the original traditional characters.
    # Mengzi
    u"𫗦": u"餔",
    u"𫛞": u"鴃",
    u"𫍙": u"訑",
    # Zhongyong
    u"𫓧": u"鈇",
    # Lunyu
    u"𫐐": u"輗",
    u"𫐄": u"軏",
    u"𫄨": u"絺",
    # The following words converted by OpenCC could not reflect its original syntax meaning.
    # Thus, modify words properly.
    # 　Mengzi
    u"将彻": u"将徹",
    u"以旗": u"以旂",
    u"关弓": u"弯弓",
    u"征招": u"徵招",
    u"遏籴": u"遏糴",
    u"逾": u"踰",
    # 　Lunyu
    u"后雕": u"后彫",
    u"不足征": u"不足徵",
    u"征之矣": u"徵之矣",
    u"絏": u"绁",
    u"不至于谷": u"不至于穀",
    u"道谷": u"道穀",
    u"旧谷": u"旧穀",
    u"新谷": u"新穀",
    u"五谷不分": u"五穀不分",
    # Daxue
    u"恂栗": u"恂慄",
    # Zhongyong
    u"半涂": u"半途",
    u"复帱": u"覆帱",
}


def Convert(content):
    for key in charAfterOpenCcConversion_to_CharShownInSimplifiedText:
        content = content.replace(
            key, charAfterOpenCcConversion_to_CharShownInSimplifiedText[key])
    return remove_redundant_subscript(content)

# 一對通假字在正體字中可以不同，但在簡體字中是一個字。所以在簡體版中，通假字標註是原字。應該去除冗餘的通假標註。
# 比如：舍~捨~：舍在正體字中是住處，比如宿舍。在經文中同“捨”，捨棄意。但是简体字中， 只有一个“舍”字，表达两个意思。
# 这样在简体字通假就失去了意义。經過轉換變成了“舍~舍~”。
# 又如：與~歟~ 這對通假字在簡體字中是通一個字。


def remove_redundant_subscript(content):
    i = 0
    while i < len(content) - 3:
        if content[i+1] == '~' and content[i+3] == '~' and content[i] == content[i+2]:
            content = content[:i+1] + content[i+4:]
        i += 1
    return content

# 入聲字： 用`^^`標誌, 比如： ^曰^。This is interpreted by [pandoc subscription
#　extension](https://pandoc.org/MANUAL.html#extension-superscript-subscript).
# Todo:
# check boundary
# move constant to global.


def mark_checked_tone_chars(book):
    result = ""
    for index, _ in enumerate(book):
        result += AncientChar(book, index).mark_checked_tone_char()
    return result


class AncientChar:
    def __init__(self, book, index):
        self.c = book[index]
        self.book = book
        self.index = index

    def mark_checked_tone_char(self):
        if self.is_checked_tone_char() and not self.is_alternative_char():
            return self.to_superscript()
        return self.c

    def is_checked_tone_char(self):
        return self.c in checkedToneChars

    def is_alternative_char(self):
        wrapped_with_pandoc_subscript_sign = self.index > 0 and self.book[self.index - 1] == '~' and self.index < (
            len(self.book) - self.index) and self.book[self.index + 1] == '~'
        return wrapped_with_pandoc_subscript_sign

    def to_superscript(self):
        return '^' + self.c + '^'


class CheckedToneChar(AncientChar):
    def __init__(self, c):
        self.c = c
