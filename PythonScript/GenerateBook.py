#Set Cover=Cover
#Set BookCover=%BookName%%Cover%
#Set BookCoverHTML=%BookCover%%HTMLExt%
#Call pandoc ..\source\%BookCover%%BookExt% -o %BookCoverHTML% --standalone %CSS_%%Cover%%CSSExt% --verbose

def GenerateCover():
	pass

if __name__ == '__main__':
	GenerateCover()
