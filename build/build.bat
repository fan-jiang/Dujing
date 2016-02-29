Set DecorateName=DecorateName
Set Book=mencius_TraditionalFont
Set FontSize=FontSize48
Set Output1=%Book%_%FontSize%_%DecorateName%
Set Output2=%Book%_%FontSize%
Set HTMLExt=.html
Set HTMLOutput1=%Output1%%HTMLExt%
Set HTMLOutput2=%Output2%%HTMLExt%

Call pandoc ..\source\mencius.md -o %HTMLOutput1% --standalone --toc --css=..\css\%DecorateName%.css --css=..\css\FontSize.css --verbose
call wkhtmltopdf.exe %HTMLOutput1% %Output1%.pdf

Call pandoc ..\source\mencius.md -o %HTMLOutput2% --standalone --toc --css=..\css\FontSize.css --verbose
call wkhtmltopdf.exe %HTMLOutput2% %Output2%.pdf