def main():
    try:
        fileName = "MengZi_Traditional.md"
        filePath = "../../source/" + fileName
        with open(filePath, 'r') as file:
            for line in file:
                print line
    except IOError:
        print ("The file (" + filePath + ") does not exist.")

if __name__ == '__main__':
    main()