Set OpenCCFolder=..\opencc-0.4.2\
Set BookExt=.md
Set Book=Mencius_
%OpenCCFolde%zht2zhs.ini
%OpenCCFolder%opencc -i %Book%Traditional%BookExt% -o %Book%Simplified%BookExt% -c %OpenCCFolde%zht2zhs.ini
Set Book=ZhongYong_
%OpenCCFolder%opencc -i %Book%Traditional%BookExt% -o %Book%Simplified%BookExt% -c %OpenCCFolde%zht2zhs.ini