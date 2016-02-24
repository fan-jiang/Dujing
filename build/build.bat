Set Output=mencius_TraditionalFont_UnemphasizedName_FontSize48
Set HTMLExt=.html
Set HTMLOutput=%Output%%HTMLExt%

Call pandoc ..\source\mencius.md -o %HTMLOutput% --standalone --toc --css=..\css\UnemphasizedName.css --css=..\css\FormatHeader.css --verbose
call wkhtmltopdf.exe %HTMLOutput% %Output%.pdf