del bonus_box_data.py
del bonus_set_data.py
del item_data.py
del fame_data.py
del consumable_item_data.py



rsync --port 11369 -a 10.240.120.155::entities/common/common_server/data/bonus_box_data.py .
rsync --port 11369 -a 10.240.120.155::entities/common/common_server/data/bonus_set_data.py .
rsync --port 11369 -a 10.240.120.155::entities/common/common_server/data/item_data.py .
rsync --port 11369 -a 10.240.120.155::entities/common/common_server/data/fame_data.py .
rsync --port 11369 -a 10.240.120.155::entities/common/common_server/data/consumable_item_data.py .

