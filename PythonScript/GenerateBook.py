import subprocess
def GenerateCover():
	Cover = "Cover"
	BookName = "BookName"
	BookCover = BookName + Cover
	BookCoverHTML = BookCover + ".html"
	CSS = "CSS_"
	CSSExt = "CSSExt"

	pandocCommand = "pandoc ..\\source\\" + BookCover + ".txt -o "
	+ BookCoverHTML + " -standalone " + CSS_ + Cover + ".css --verbose"
	subprocess.call(pandocCommand, stdout=FNULL, stderr=FNULL, shell=False)

if __name__ == '__main__':
	GenerateCover()
