Set Book=%BookName%%1
Call Generate %Book% name SongTi FontSize48
Call Generate %Book% name QuanZiKuFont FontSize48
Call Generate %Book% name BeiShiDaFont FontSize48
Call Generate %Book% name JinWen FontSize48
Call Generate %Book% name LiShu FontSize48
Call Generate %Book% name JiaGuWen FontSize48
Call Generate %Book% name JinWen FontSize96
Set Destinaton=%OutputFolder%\%1
MkDir %Destinaton%
Move /Y %Book%*.pdf %Destinaton%