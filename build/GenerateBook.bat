Set BookName=%1_
Set BookPath=%SourceFolder%%BookName%
%OpenCCFolder%opencc -i %BookPath%%T%%BookExt% -o %BookPath%%S%%BookExt% -c %OpenCCFolde%zht2zhs.ini
Set OutputFolder=..\ÖÐÎÄ½›µä\%1

Set Book=%BookName%%T%
Call Generate %Book%
Set Destinaton=%OutputFolder%\%T%
MkDir %Destinaton%
Move /Y %1_*.pdf %Destinaton%

Set Book=%BookName%%S%
Call Generate %Book%
Set Destinaton=%OutputFolder%\%S%
MkDir %Destinaton%
Move /Y %1_*.pdf %Destinaton%

