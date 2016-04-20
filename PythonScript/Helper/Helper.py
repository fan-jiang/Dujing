# This Python file uses the following encoding: utf-8

def Convert(content):
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
        u"將彻":u"將徹",
        u"以旗":u"以旂",
        u"关弓":u"弯弓",
        u"征招":u"徵招",
        u"遏籴":u"遏糴",
        u"逾":u"踰",
    }
    for key in tradtionalToSimplified: 
        content = content.replace(key, tradtionalToSimplified[key])
    return content

def main():
    try:
        fileName = "Test_Simplified.md"
        filePath = "../../source/" + fileName
        content = None
        with open(filePath,'r') as file:
            content = file.read().decode("utf-8")
        content = Convert(content)
        with open(filePath,'w') as file:
            file.write(content.encode("utf-8"))
        print "OK"
    except IOError:
        print ("IOError occurs while handling the file (" + filePath + ").")

if __name__ == '__main__':
    main()