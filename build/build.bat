Set DecorateName=DecorateName
Set CSSExt=.css
Set CSS_=--css=..\css\
Set NameStyle=%CSS_%%DecorateName%%CSSExt%
Set Style=%CSS_%Common%CSSExt%

If Not "%1" == "" (
	Set Output=%Book%
)

If "%2" == "name" (
	Set Output=%Output%_%DecorateName%
	Set Style=%Style% %NameStyle%
)

If Not "%3" == "" (
	Set Output=%Output%_%3
	Set Style=%Style% %CSS_%%3%CSSExt%
)

If Not "%4" == "" (
	Set Output=%Output%_%4
	Set Style=%Style% %CSS_%%4%CSSExt%
)

Set HTMLExt=.html
Set HTMLOutput=%Output%%HTMLExt%

Call pandoc ..\source\%Book%.md -o %HTMLOutput% --standalone %Style% --verbose
Call wkhtmltopdf.exe --margin-top 15 --header-spacing 5 --header-left [section] --header-right [subsection] --header-line --margin-bottom 15 --footer-spacing 5 --footer-left "Dujing Academy" --footer-right [page]/[topage] --footer-line --footer-font-size 5 toc %HTMLOutput% %Output%.pdf