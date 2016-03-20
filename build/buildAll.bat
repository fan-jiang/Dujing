:: Stop PDF reader
TaskKill /f /im AcroRd32.exe

:: Convert to the simplified text
Set OpenCCFolder=..\opencc-0.4.2\
Set SourceFolder=..\Source\
Set BookExt=.md
Set T=Traditional
Set S=Simplified
Set BookName=Mencius_
Set BookPath=%SourceFolder%%BookName%
%OpenCCFolder%opencc -i %BookPath%%T%%BookExt% -o %BookPath%%S%%BookExt% -c %OpenCCFolde%zht2zhs.ini

:: Generate Book
Set Book=%BookName%%T%
Call build %Book%
Set Book=%BookName%%S%
Call build %Book%

Set BookName=ZhongYong_
Set BookPath=%SourceFolder%%BookName%
%OpenCCFolder%opencc -i %BookPath%%T%%BookExt% -o %BookPath%%S%%BookExt% -c %OpenCCFolde%zht2zhs.ini
Set Book=%BookName%%T%
Call build %Book%
Set Book=%BookName%%S%
Call build %Book%

::Call build name SongTi FontSize48
::Call build name QuanZiKuFont FontSize48
::Call build name BeiShiDaFont FontSize48
::Call build name JinWen FontSize48
::Call build name LiShu FontSize48
::Call build name JiaGuWen FontSize48
::Call build name JinWen FontSize96

::Del *.html