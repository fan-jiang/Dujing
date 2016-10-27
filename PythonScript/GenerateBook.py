import subprocess
import os


def GenerateBook():
	Books = ["DaXue", "ZhongYong", "LunYu", "MengZi"]
	prefaceCommand = "pandoc ..\\Source\\Preface.md -o Preface.html --standalone"
	with open("Dujing.log", 'w') as trace:
		subprocess.call(prefaceCommand, stdin=None, stdout=trace, stderr=None, shell=True)
		os.chdir("..\\Build")
		for book in Books:
			subprocess.call("GenerateBook " + book, stdin=None, stdout=trace, stderr=None, shell=True)

if __name__ == '__main__':
	GenerateBook()
