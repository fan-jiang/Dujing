# This Python file uses the following encoding: utf-8

import sys
import Convert

def main():
    try: 
        filePath = sys.argv[1]
        content = None
        with open(filePath,'r') as file:
            content = file.read().decode("utf-8")
        content = Convert.Convert(content)
        with open(filePath,'w') as file:
            file.write(content.encode("utf-8"))
    except IOError:
        print ("IOError occurs while handling the file (" + filePath + ").")

if __name__ == '__main__':
    main()