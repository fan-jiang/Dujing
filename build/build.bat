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

Call pandoc ..\source\%Book%.md -o %HTMLOutput% --standalone %Style% --verbose
Call wkhtmltopdf.exe --margin-top 15 --header-spacing 5 --header-right [subsection] --header-line --margin-bottom 15 --footer-spacing 5 --footer-left "Dujing Academy" --footer-right [page]/[topage] --footer-line --footer-font-size 5 toc %HTMLOutput% %Output%.pdf