# This Python file uses the following encoding: utf-8

import sys
import getopt
import Convert


def usage():
	print "Usage: to be done."

def main(argv):

	try:
		opts, args = getopt.getopt(argv, "hb:d", ["help", "book="])
	except getopt.GetoptError:
		usage()
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			usage()
			sys.exit(2)
		elif opt == "-d":
			global _debug
			_debug = 1
		elif opt in ("-b","--book"):
			filePath = arg

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
	main(sys.argv[1:])