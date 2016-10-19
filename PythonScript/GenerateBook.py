import subprocess
def GenerateCover():
	Cover = "Cover"
	BookName = "BookName"
	BookCover = BookName + Cover
	BookExt = "BookExt"
	HTMLExt = "HTMLExt"
	BookCoverHTML = BookCover + HTMLExt
	CSS = "CSS_"
	CSSExt = "CSSExt"

	pandocCommand = "pandoc ..\\source\\" + BookCover + BookExt + " -o "
	+ BookCoverHTML + " -standalone " + CSS_ + Cover + CSSExt + " --verbose"
	subprocess.call(pandocCommand, stdout=FNULL, stderr=FNULL, shell=False)

if __name__ == '__main__':
	GenerateCover()
