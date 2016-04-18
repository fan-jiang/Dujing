# This Python file uses the following encoding: utf-8

def Convert(content):
    tradtionalToSimplified = {
        u"「":u"“", 
        u"」":u"”",
        u"『":u"‘",
        u"』":u"’",
        "\uf0ab97a6":u"餔",
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