Set OpenCCFolder=..\opencc-0.4.2\
Set BookExt=.txt
Set S=Simplified
Call %OpenCCFolder%opencc -i %1 -o %1_%S%%BookExt% -c %OpenCCFolder%zht2zhs.ini