import subprocess
import os
import logging
from time import clock

logging.basicConfig(filename='classicor.log', level=logging.DEBUG)

def GenerateBook():
	Books = ["DaXue", "ZhongYong", "LunYu", "MengZi"]
	prefaceCommand = "pandoc ..\\Source\\Preface.md -o Preface.html --standalone"
	with open("dujing.log", 'w') as trace:
		subprocess.call(prefaceCommand, stdin=None, stdout=trace, stderr=None, shell=True)
		os.chdir("..\\Build")
		for book in Books:
			logging.info('Generating books for ' + book + '...')
		subprocess.call("GenerateBook " + book, stdin=None, stdout=trace, stderr=None, shell=True)

if __name__ == '__main__':
	start_time = clock()
	GenerateBook()
	print("The execution during is: %s seconds" % (clock() - start_time))
