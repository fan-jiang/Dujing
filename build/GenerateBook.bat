Set SourceFolder=..\Source\
Set BookExt=.txt
Set T=Traditional
Set S=Simplified
Set BookName=%1_
Set BookPath=%SourceFolder%%BookName%

:: Update the traditional source file
Set TraditionalText=%BookPath%%T%%BookExt%
Call ..\PythonScript\UpdateFile.py %T% %TraditionalText%
:: Generate the simplified source file
Set OpenCCFolder=..\opencc-0.4.2\
Set SimplifiedText=%BookPath%%S%%BookExt%
Call %OpenCCFolder%opencc -i %TraditionalText% -o %SimplifiedText% -c %OpenCCFolder%zht2zhs.ini
Call ..\PythonScript\UpdateFile.py %S% %SimplifiedText%

:: Generate book
Set OutputFolder=Output\%1
Call GenerateBookHelper %T%
Call GenerateBookHelper %S%
