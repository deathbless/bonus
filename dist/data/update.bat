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
:�˵�
cls

set ѡ��=%1
if %ѡ��%==1 set %srvname=mg
if %ѡ��%==2 set %srvname=zfy
if %ѡ��%==3 set %srvname=wjh
if %ѡ��%==4 set %srvname=cw
if %ѡ��%==5 set %srvname=hzruanyang
if %ѡ��%==6 set %srvname=mjq
if %ѡ��%==7 set %srvname=common
if %ѡ��%==8 set %srvname=pwf
if %ѡ��%==9 set %srvname=lianaku
if %ѡ��%==10 set %srvname=czq
if %ѡ��%==11 set %srvname=yf
if %ѡ��%==12 set %srvname=xxc
if %ѡ��%==13 set %srvname=cyg
if %ѡ��%==14 set %srvname=zw
if %ѡ��%==15 set %srvname=syj
if %ѡ��%==16 set %srvname=yck
if %ѡ��%==17 goto syncwa
goto syncsf


:syncsf
echo ����ͬ�� %srvname%��
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
echo �������

