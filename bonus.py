#coding=utf-8
__author__ = 'hzsunyuda'
import re
import os
import easygui

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

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
    table = 10000
    if box.has_key('itemSetInfo'):
        str = "奖励分组_数据表(itemSetInfo):\n"
        ans.append(str)
        item = bsd.data[box['itemSetInfo'][0]]

        for bonus in item:
            tstr = "    "
            type = ""
            t_type = bonus['bonusType']
            if t_type == 1:
                type = "物品"
            elif t_type == 2:
                type = "金钱"
            elif t_type == 3:
                type = "声望"
            elif t_type == 4:
                type = "经验"
            elif t_type == 6:
                type = "社会经验"
            else:
                type = "无类型"

            name = id.data[bonus['bonusId']]['name']
            # name = name.encode("utf-8")
            # tlen = len(name)
            tid = bonus["bonusId"]

            temp = ("物品ID：%d    " % tid)
            tstr += temp

            temp = ("类型：%s    " % type)
            tstr += temp

            if bonus['calcType'] == 1:
                tstr += "分配方式：圆桌分配    "
            elif bonus['calcType'] == 2:
                tstr += "分配方式：分别计算    "

            rate = bonus['bonusRate']
            if bonus['calcType'] == 1:
                if table >= rate:
                    table -= rate
                else:
                    rate = table
                    table = 0

            temp = ("掉落几率(万分率)：%d    " % (rate))
            tstr += temp

            if t_type == 2 or t_type == 3:
                minNum = bonus['minBonusFormula']
                maxNum = bonus['maxBonusFormula ']
                temp = ("掉落数量(最小~最大)：%s ~ %s    " % (minNum,maxNum))
                tstr += temp
            else:
                minNum = bonus['minBonusNum']
                maxNum = bonus['maxBonusNum']
                temp = ("掉落数量(最小~最大)：%d ~ %d    " % (minNum,maxNum))
                tstr += temp


            temp = ("物品名称：%s    " % (name))
            # if tlen <= 30:
            #     temp += " " * (30 - tlen)
            tstr += temp
            ans.append(tstr)




    if box.has_key('itemBoxInfo'):
        str = "公共奖励包_配置表(itemBoxInfo):\n"
        ans.append(str)
        item = bbd.data[box['itemBoxInfo'][0]]
        for bonus in item:
            tstr = "    "
            minlv = bonus['lvStart']
            maxlv = bonus['lvEnd']
            temp = ("等级限制(最低~最高)：%d ~ %d    " % (minlv,maxlv))
            tstr += temp
            if bonus.has_key('itemBonus'):

                itemBonus = bonus['itemBonus']

                name = id.data[itemBonus[0]]['name']
                # name = name.encode("utf-8","ignore")

                tid = itemBonus[0]
                temp = ("物品ID：%d    " % tid)
                tstr += temp

                temp = ("物品类型：物品    ")
                tstr += temp

                rate = itemBonus[1]
                temp = ("掉落几率(万分率)：%d    " % (rate))
                tstr += temp

                minNum = itemBonus[2]
                maxNum = itemBonus[3]
                temp = ("掉落数量(最小~最大)：%s ~ %s    " % (minNum,maxNum))
                tstr += temp

                temp = ("物品名称：%s    " % (name))
                tstr += temp

            if bonus.has_key('bonusSets') and bonus.has_key('itemBonus'):
                tstr += '\n\n'

            if bonus.has_key('bonusSets'):
                bonusSet = bonus['bonusSets']
                num = 1
                for Set in bonusSet:
                    temp = "    物品分组表%d —— " % num
                    num = num + 1

                    tstr += temp
                    type = bonus['calcType']
                    if type == 1:
                        temp = "分配方式：分别计算    "
                    if type == 2:
                        temp = "分配方式：圆桌分配    "
                    tstr += temp

                    bonusnum = Set[0]
                    rate = Set[1]
                    temp = "掉落几率(万分率)：%d    \n        " % rate
                    tstr += temp

                    item = bsd.data[bonusnum]
                    for bonus in item:
                        type = ""
                        t_type = bonus['bonusType']
                        if t_type == 1:
                            type = "物品"
                        elif t_type == 2:
                            type = "金钱"
                        elif t_type == 3:
                            type = "声望"
                        elif t_type == 4:
                            type = "经验"
                        elif t_type == 6:
                            type = "社会经验"
                        else:
                            type = "无类型"

                        name = id.data[bonus['bonusId']]['name']
                        # name = name.encode("utf-8","ignore")
                        # tlen = len(name)
                        tid = bonus["bonusId"]

                        temp = ("物品ID：%d    " % tid)
                        tstr += temp

                        temp = ("类型：%s    " % type)
                        tstr += temp

                        if bonus['calcType'] == 1:
                            tstr += "分配方式：圆桌分配    "
                        elif bonus['calcType'] == 2:
                            tstr += "分配方式：分别计算    "

                        rate = bonus['bonusRate']
                        if bonus['calcType'] == 1:
                            if table >= rate:
                                table -= rate
                            else:
                                rate = table
                                table = 0

                        temp = ("掉落几率(万分率)：%d    " % (rate))
                        tstr += temp

                        if t_type == 2 or t_type == 3:
                            minNum = bonus['minBonusFormula']
                            maxNum = bonus['maxBonusFormula ']
                            temp = ("掉落数量(最小~最大)：%s ~ %s    " % (minNum,maxNum))
                            tstr += temp
                        else:
                            minNum = bonus['minBonusNum']
                            maxNum = bonus['maxBonusNum']
                            temp = ("掉落数量(最小~最大)：%d ~ %d    " % (minNum,maxNum))
                            tstr += temp


                        temp = ("物品名称：%s    \n        " % (name))
                        tstr += temp
                        # if tlen <= 30:
                        #     temp += " " * (30 - tlen)


                    temp = "\n——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————\n\n"
                    tstr += temp








            ans.append(tstr)



    str = ""
    for a in range(0,ans.__len__()):
        # ans[a] = ans[a].encode("utf-8","ignore")
        str += ans[a]+"\n"


    easygui.textbox("编号为%d的宝箱查询到以下结果" % input_cid,"结果",str,codebox=1)
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
    os.system("pause")



