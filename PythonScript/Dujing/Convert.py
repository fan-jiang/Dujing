# This Python file uses the following encoding: utf-8

tradtionalToSimplified = {
# Simplified text has its own quotation marks.
        u"「":u"“",
        u"」":u"”",
        u"『":u"‘",
        u"』":u"’",
# OpenCC successfully converts the following characters to the simplified UTF-8 code.
# However, they could not be shown in most of Chinese Font families.
# Thus, the traditional characters are used.
## Mengzi 
        u"𫗦":u"餔",
        u"𫛞":u"鴃",
        u"𫍙":u"訑",
## Zhongyong
        u"𫓧":u"鈇",
## Lunyu
        u"𫐐":u"輗",
        u"𫐄":u"軏",
        u"𫄨":u"絺",
# The following words converted by OpenCC are correct, but
# the conversion affects the syntax meaning.
# The word should be modified.
##　Mengzi
        u"将彻":u"将徹",
        u"以旗":u"以旂",
        u"关弓":u"弯弓",
        u"征招":u"徵招",
        u"遏籴":u"遏糴",
        u"逾":u"踰",
##　Lunyu
        u"后雕":u"后彫",
        u"不足征":u"不足徵",
        u"征之矣":u"徵之矣",
        u"絏":u"绁",
        u"不至于谷":u"不至于穀",
        u"道谷":u"道穀",
        u"旧谷":u"旧穀",
        u"新谷":u"新穀",
        u"五谷不分":u"五穀不分",
## Daxue
        u"恂栗":u"恂慄",
## Zhongyong
        u"半涂":u"半途",
        u"复帱":u"覆帱",
## Ignore un-needed subscripts
        u"舍~舍~":u"舍",
}

def Convert(content):
    for key in tradtionalToSimplified:
        content = content.replace(key, tradtionalToSimplified[key])
    return content

def remove_redundant_subscript(content):
    return u"舍"
