TaskKill /f /im AcroRd32.exe
Set T=Traditional
Set S=Simplified
Set BookName=mencius_
Call build %BookName%%T%
Call build %BookName%%S%
Set BookName=ZhongYong_
Call build %BookName%%T%
Call build %BookName%%S%

::Call build name SongTi FontSize48
::Call build name QuanZiKuFont FontSize48
::Call build name BeiShiDaFont FontSize48
::Call build name JinWen FontSize48
::Call build name LiShu FontSize48
::Call build name JiaGuWen FontSize48
::Call build name JinWen FontSize96

::Del *.html