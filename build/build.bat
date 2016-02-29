Set DecorateName=DecorateName
Set Book=mencius
Set FontType=Traditional
Set FontSize=FontSize48
Set BookFont=%Book%_%FontType%_%FontSize%
Set CSSExt=.css
Set CSS_=--css=..\css\
Set FontSizeStyle=%CSS_%FontSize%CSSExt%
Set NameStyle=%CSS_%%DecorateName%%CSSExt%
Set Output=%BookFont%
Set Style=%FontSizeStyle% 

If "%1" == "name" (
	Set Output=%Output%_%DecorateName%
	Set Style=%Style% %NameStyle%
)

Set HTMLExt=.html
Set HTMLOutput=%Output%%HTMLExt%

Call pandoc ..\source\%Book%.md -o %HTMLOutput% --standalone --toc %Style% --verbose
Call wkhtmltopdf.exe %HTMLOutput% %Output%.pdf