Set Book=%BookName%%1
Call Generate %Book% KaiTi FontSize48 Name
Call Generate %Book% KaiTi
Call Generate %Book% SongTi

:: The following fonts generated unreadable characters.
REM Call Generate %Book% FangSong
REM Call Generate %Book% QuanZiKuFont

:: The following fonts generated incomplete text.
REM Call Generate %Book% BeiShiDaFont
REM Call Generate %Book% JinWen
REM Call Generate %Book% LiShu
REM Call Generate %Book% JiaGuWen

Set Destination=%OutputFolder%\%1
RmDir %Destination% /s /q
MkDir %Destination%
Move /Y *.pdf  %Destination%
Move /Y *.mobi %Destination%