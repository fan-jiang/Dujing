# This Python file uses the following encoding: utf-8

def Convert(content):
    tradtionalToSimplified = {
        u"「":u"“", 
        u"」":u"”",
        u"『":u"‘",
        u"』":u"’",
        u"𫗦":u"餔",
        u"𫛞":u"鴃",
        u"𫍙":u"訑",
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