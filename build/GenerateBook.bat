Set BookName=%1_
Set BookPath=%SourceFolder%%BookName%
:: Generate the simplified source file
Set OpenCCFolder=..\opencc-0.4.2\
Set SimplifiedText=%BookPath%%S%%BookExt%
Call %OpenCCFolder%opencc -i %BookPath%%T%%BookExt% -o %SimplifiedText% -c %OpenCCFolde%zht2zhs.ini
Call python ..\PythonScript\Helper\Helper.py --book %SimplifiedText%
Set OutputFolder=Output\%1
Call GenerateBookHelper %T%
Call GenerateBookHelper %S%


