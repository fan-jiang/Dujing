Set SourceFolder=..\Source\
Set BookExt=.txt
Set T=Traditional
Set S=Simplified
Set BookName=%1_
Set BookPath=%SourceFolder%%BookName%

:: Generate the simplified source file
Set OpenCCFolder=..\opencc-0.4.2\
Set SimplifiedText=%BookPath%%S%%BookExt%
Call %OpenCCFolder%opencc -i %BookPath%%T%%BookExt% -o %SimplifiedText% -c %OpenCCFolder%zht2zhs.ini
Call ..\PythonScript\ConvertFile.py %SimplifiedText%

:: Generate book
Set OutputFolder=Output\%1
Call GenerateBookHelper %T%
Call GenerateBookHelper %S%


