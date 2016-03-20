:: Stop PDF reader
TaskKill /f /im AcroRd32.exe

Set OpenCCFolder=..\opencc-0.4.2\
Set SourceFolder=..\Source\
Set BookExt=.md
Set T=Õýów
Set S=º†ów

Call GenerateBook ÃÏ×Ó
Call GenerateBook ÖÐÓ¹

::Call build name SongTi FontSize48
::Call build name QuanZiKuFont FontSize48
::Call build name BeiShiDaFont FontSize48
::Call build name JinWen FontSize48
::Call build name LiShu FontSize48
::Call build name JiaGuWen FontSize48
::Call build name JinWen FontSize96

Del *.html
Del %SourceFolder%*%S%%BookExt%