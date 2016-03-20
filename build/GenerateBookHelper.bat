Set Book=%BookName%%1
Call Generate %Book%
Set Destinaton=%OutputFolder%\%1
MkDir %Destinaton%
Move /Y %Book%*.pdf %Destinaton%