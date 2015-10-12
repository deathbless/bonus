@echo off
del bonus_box_data.py
del bonus_set_data.py
del item_data.py
del fame_data.py
del consumable_item_data.py
del bonus_data.py
del treasure_box_data.py
del box_bonus_map_data.py
del game_item_limit_data.py
:菜单
cls

set 选择=%1
if %选择%==1 set %srvname=mg
if %选择%==2 set %srvname=zfy
if %选择%==3 set %srvname=wjh
if %选择%==4 set %srvname=cw
if %选择%==5 set %srvname=hzruanyang
if %选择%==6 set %srvname=mjq
if %选择%==7 set %srvname=common
if %选择%==8 set %srvname=pwf
if %选择%==9 set %srvname=lianaku
if %选择%==10 set %srvname=czq
if %选择%==11 set %srvname=yf
if %选择%==12 set %srvname=xxc
if %选择%==13 set %srvname=cyg
if %选择%==14 set %srvname=zw
if %选择%==15 set %srvname=syj
if %选择%==16 set %srvname=yck
if %选择%==17 goto syncwa
goto syncsf


:syncsf
echo 正在同步 %srvname%服
rsync --port 11369 -a 10.240.120.155::entities/%srvname%/common_server/data/bonus_box_data.py .
rsync --port 11369 -a 10.240.120.155::entities/%srvname%/common_server/data/bonus_set_data.py .
rsync --port 11369 -a 10.240.120.155::entities/%srvname%/common_server/data/item_data.py .
rsync --port 11369 -a 10.240.120.155::entities/%srvname%/common_server/data/fame_data.py .
rsync --port 11369 -a 10.240.120.155::entities/%srvname%/common_server/data/consumable_item_data.py .
rsync --port 11369 -a 10.240.120.155::entities/%srvname%/common_server/data/bonus_data.py .
rsync --port 11369 -a 10.240.120.155::entities/%srvname%/common_server/data/treasure_box_data.py .
rsync --port 11369 -a 10.240.120.155::entities/%srvname%/common_server/data/box_bonus_map_data.py .
rsync --port 11369 -a 10.240.120.155::entities/%srvname%/common_server/data/game_item_limit_data.py .
goto end

:end
echo 更新完毕

