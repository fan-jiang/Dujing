# This Python file uses the following encoding: utf-8
def main():
    try:
        fileName = "MengZi_Traditional.md"
        filePath = "../../source/" + fileName
        content = None
        with open(filePath,'r') as file:
            content = file.read().decode("utf-8")
        content = content.replace(u"「",u'“')
        content = content.replace(u"」",u'”')
        content = content.replace(u"『",u'‘')
        content = content.replace(u"』",u'’')
        with open(filePath,'w') as file:
            file.write(content.encode("utf-8"))
        print "OK"
    except IOError:
        print ("IOError occurs while handling the file (" + filePath + ").")

if __name__ == '__main__':
    main()