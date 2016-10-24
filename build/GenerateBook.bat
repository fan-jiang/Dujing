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
Call python ..\PythonScript\Dujing\Dujing.py %SimplifiedText%
Set OutputFolder=Output\%1
Call GenerateBookHelper %T%
Call GenerateBookHelper %S%


