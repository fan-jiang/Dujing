Set SourceFolder=..\Source\
Set BookExt=.md
Set T=Õýów
Set S=º†ów
Set BuildLog=BuildLog.txt
@echo Build begins at: %DATE% %TIME% > %BuildLog%
Set STARTTIME=%TIME%
:: Stop PDF reader
TaskKill /f /im AcroRd32.exe
Call GenerateBook ÃÏ×Ó >> %BuildLog%
Call GenerateBook ÖÐÓ¹ >> %BuildLog%

::Call build name SongTi FontSize48
::Call build name QuanZiKuFont FontSize48
::Call build name BeiShiDaFont FontSize48
::Call build name JinWen FontSize48
::Call build name LiShu FontSize48
::Call build name JiaGuWen FontSize48
::Call build name JinWen FontSize96

:: Clean up
Del *.html
Del %SourceFolder%*%S%%BookExt%

@echo off
Set ENDTIME=%TIME%
:: Change formatting for the start and end times
for /F "tokens=1-4 delims=:.," %%a in ("%STARTTIME%") do (
   set /A "start=(((%%a*60)+1%%b %% 100)*60+1%%c %% 100)*100+1%%d %% 100"
)

for /F "tokens=1-4 delims=:.," %%a in ("%ENDTIME%") do (
   set /A "end=(((%%a*60)+1%%b %% 100)*60+1%%c %% 100)*100+1%%d %% 100"
)

:: Calculate the elapsed time by subtracting values
set /A elapsed=end-start

:: Format the results for output
set /A hh=elapsed/(60*60*100), rest=elapsed%%(60*60*100), mm=rest/(60*100), rest%%=60*100, ss=rest/100, cc=rest%%100
if %hh% lss 10 set hh=0%hh%
if %mm% lss 10 set mm=0%mm%
if %ss% lss 10 set ss=0%ss%
if %cc% lss 10 set cc=0%cc%

Set DURATION=%hh%:%mm%:%ss%,%cc%

echo Start    : %STARTTIME%
echo Finish   : %ENDTIME%
echo          ---------------
echo Duration : %DURATION% 

@echo Build ends at: %DATE% %TIME% >> %BuildLog%







