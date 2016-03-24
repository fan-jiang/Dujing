Set BookName=%1_
Set BookPath=%SourceFolder%%BookName%
:: Generate the simplified source file
Set OpenCCFolder=..\opencc-0.4.2\
Call %OpenCCFolder%opencc -i %BookPath%%T%%BookExt% -o %BookPath%%S%%BookExt% -c %OpenCCFolde%zht2zhs.ini

Set OutputFolder=%1
Call GenerateBookHelper %T%
Call GenerateBookHelper %S%


