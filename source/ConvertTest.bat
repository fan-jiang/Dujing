Set OpenCCFolder=..\opencc-0.4.2\
Set BookExt=.md
Set BookPath=..\%1
Set S=Simplified
Call %OpenCCFolder%opencc -i %1 -o Test_Simplified.md -c %OpenCCFolde%zht2zhs.ini