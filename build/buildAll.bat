TaskKill /f /im AcroRd32.exe
Set T=Traditional
Set S=Simplified
Set BookName=Mencius_
Set Book=%BookName%%T%
Call build %Book%
Set Book=%BookName%%S%
Call build %Book%
Set BookName=ZhongYong_
Set Book=%BookName%%T%
Call build %Book%
Set Book=%BookName%%S%
Call build %Book%

::Call build name SongTi FontSize48
::Call build name QuanZiKuFont FontSize48
::Call build name BeiShiDaFont FontSize48
::Call build name JinWen FontSize48
::Call build name LiShu FontSize48
::Call build name JiaGuWen FontSize48
::Call build name JinWen FontSize96

::Del *.html