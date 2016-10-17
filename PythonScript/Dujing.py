# This Python file uses the following encoding: utf-8

import sys
import argparse
import Convert

def main():
	parser = argparse.ArgumentParser(description='Generate a classic book with the desired format.')
	parser.add_argument('book', type=str, help='a book file')
	args = parser.parse_args()
	filePath = args.book
	try:
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
