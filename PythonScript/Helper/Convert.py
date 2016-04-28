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
        u"后凋":u"后彫",
## Daxue
        u"恂栗":u"恂慄",
}

def Convert(content):
    for key in tradtionalToSimplified: 
        content = content.replace(key, tradtionalToSimplified[key])
    return content