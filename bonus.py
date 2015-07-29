__author__ = 'hzsunyuda'
import re

import easygui

from data import bonus_box_data as bbd
from data import bonus_set_data as bsd
from data import consumable_item_data as cid
from data import item_data as id


def search(input_cid):
    box = 0
    if cid.data.has_key(input_cid):
        box = cid.data[input_cid]
    else:
        easygui.msgbox("没有查找到此ID!")
        mainsearch()
        return

    ans = []
    type = ""
    if box.has_key('itemSetInfo'):
        str = u"奖励分组_数据表(itemSetInfo):\n"
        ans.append(str)
        item = bsd.data[box['itemSetInfo'][0]]
        for bonus in item:
            ans.append(id.data[bonus["bonusId"]]['name'])
        type = "itemSetInfo"



    if box.has_key('itemBoxInfo'):
        str = u"公共奖励包_配置表(itemSetInfo):\n"
        ans.append(str)
        item = bbd.data[box['itemBoxInfo']]
        for bonus in item:
            ans.append(id.data[bonus["dpItemId"]]['name'])
    str = ""
    for a in range(0,ans.__len__()):
        ans[a] = ans[a].encode("utf-8","ignore")
        str += ans[a]+"\n"


    easygui.textbox("查询到以下结果","结果",str)
    mainsearch()

def check(str):
    if re.match('^[0-9]+$',str):
        return True
    else:
        return False

def mainsearch():
    a = easygui.enterbox("请输入要查找的ID","查找")
    if a == None:
        return
    if check(a) and a != "":
        search(int(a))
    else:
        easygui.msgbox("请输入数字！")
        mainsearch()

if __name__ == '__main__':
    mainsearch()



