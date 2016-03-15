Set DecorateName=DecorateName
Set Book=mencius
Set FontType=Traditional
Set BookFont=%Book%_%FontType%
Set CSSExt=.css
Set CSS_=--css=..\css\
Set NameStyle=%CSS_%%DecorateName%%CSSExt%
Set Output=%BookFont%

If "%1" == "name" (
	Set Output=%Output%_%DecorateName%
	Set Style=%NameStyle%
)

If Not "%2" == "" (
	Set Output=%Output%_%2
	Set Style=%Style% %CSS_%%2%CSSExt%
)

If Not "%3" == "" (
	Set Output=%Output%_%3
	Set Style=%Style% %CSS_%%3%CSSExt%
)

Set HTMLExt=.html
Set HTMLOutput=%Output%%HTMLExt%

Call pandoc ..\source\%Book%.md -o %HTMLOutput% --standalone --toc %Style% --verbose
Call wkhtmltopdf.exe --margin-top 15 --margin-bottom 15 --header-center [section] --header-left [subsection] --header-right [page] --header-line --header-spacing 5 --footer-center "Version 0.1" --footer-line --footer-spacing 5 %HTMLOutput% %Output%.pdf