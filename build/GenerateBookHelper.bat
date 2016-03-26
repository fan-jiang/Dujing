Set Book=%BookName%%1
Call Generate %Book% name SongTi FontSize48
Call Generate %Book% name QuanZiKuFont FontSize48

:: The following fonts generated unreadable characters.
:: Call Generate %Book% name FangSong FontSize48
:: Call Generate %Book% name KaiTi FontSize48

:: The following fonts generated incomplete text.
REM Call Generate %Book% name BeiShiDaFont FontSize48
REM Call Generate %Book% name JinWen FontSize48
REM Call Generate %Book% name LiShu FontSize48
REM Call Generate %Book% name JiaGuWen FontSize48

Set Destinaton=%OutputFolder%\%1
:: RmDir %Destinaton% /s /q
MkDir %Destinaton%
Move /Y %Book%*.pdf %Destinaton%