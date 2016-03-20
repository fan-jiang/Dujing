Set BookName=%1_
Set BookPath=%SourceFolder%%BookName%
%OpenCCFolder%opencc -i %BookPath%%T%%BookExt% -o %BookPath%%S%%BookExt% -c %OpenCCFolde%zht2zhs.ini
Set Book=%BookName%%T%
Call Generate %Book%
Set Book=%BookName%%S%
Call Generate %Book%