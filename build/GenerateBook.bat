Set BookName=%1_
Set BookPath=%SourceFolder%%BookName%
%OpenCCFolder%opencc -i %BookPath%%T%%BookExt% -o %BookPath%%S%%BookExt% -c %OpenCCFolde%zht2zhs.ini
Set Book=%BookName%%T%
Call build %Book%
Set Book=%BookName%%S%
Call build %Book%