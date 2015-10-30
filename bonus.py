#coding=utf-8
__author__ = 'hzsunyuda'
import re
import os
import easygui

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class data:
    def __init__(self):
        data = {}

bbd = data()
bsd = data()
cid = data()
id = data()
tbd = data()
bd = data()
bbmd = data()
gild = data()

school = {3:'圣堂',4:'玉虚',5:'光刃',6:'炎天',7:'玲珑',8:'流光'}
bindType = {0:"无绑定概念",1:'获得绑定',2:'装备后绑定',3:'使用后绑定',4:'公会绑定'}
limitInterval = {1:'每天',2:'每周',3:'永久',4:'每月',5:'每季度'}

def readFile(name):
    try:
        f = file("./data/"+name)
        exec(f.read())
        return data
    except IOError:
        easygui.msgbox("缺少名字为%s的文件！请重新更新！" % name,"错误")
        exit(0)

def init():
    global bbd,bsd,cid,id,tbd,bd,bbmd,gild

    bbd.data = readFile("bonus_box_data.py")
    bsd.data = readFile("bonus_set_data.py")
    cid.data = readFile("consumable_item_data.py")
    id.data = readFile("item_data.py")
    bbd.data = readFile("bonus_box_data.py")
    tbd.data = readFile("treasure_box_data.py")
    bd.data = readFile("bonus_data.py")
    bbmd.data = readFile("box_bonus_map_data.py")
    gild.data = readFile("game_item_limit_data.py")


def checkLimit(itemSet, itemId):
    index = (itemSet,itemId)
    if gild.data.has_key(index):
        num = gild.data[index]['maxNum']
        return "全服投放%d个" % num
    else:
        return "无"


def itemSetInfo(index,level):
    ans = []
    str = "奖励分组_数据表(itemSetInfo):\n"
    ans.append(str)
    item = bsd.data[index]
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
        bind = bindType[id.data[bonus['bonusId']]['bindType']]
        tid = bonus["bonusId"]
        limit = checkLimit(index,tid)

        temp = ("物品ID：%d    " % tid)
        tstr += temp

        temp = ("类型：%s    " % type)
        tstr += temp

        if bonus['calcType'] == 1:
            tstr += "分配方式：圆桌分配    "
        elif bonus['calcType'] == 2:
            tstr += "分配方式：分别计算    "

        rate = bonus['bonusRate']
        temp = ("掉落几率(万分率)：%d    " % (rate))
        tstr += temp
        if bonus.has_key('minBonusFormula') and bonus.has_key('maxBonusFormula'):
            lv = level
            calcmin = eval(minNum)
            calcmax = eval(maxNum)
            temp = ("掉落数量(最小~最大)：%s = %d ~ %s = %d    " % (minNum,calcmin,maxNum,calcmax))
            tstr += temp
        else:
            minNum = bonus['minBonusNum']
            maxNum = bonus['maxBonusNum']
            temp = ("掉落数量(最小~最大)：%d ~ %d    " % (minNum,maxNum))
            tstr += temp
        temp = ("物品名称：%s    绑定类型：%s    投放限制：%s    " % (name,bind,limit))
        # if tlen <= 30:
        #     temp += " " * (30 - tlen)
        tstr += temp
        ans.append(tstr)
    return ans

def itemBoxInfo(index,level):
    ans = []
    str = "公共奖励包_配置表(itemBoxInfo):\n"
    ans.append(str)
    item = bbd.data[index]
    for bonus in item:
        tstr = "    "
        minlv = bonus['lvStart']
        maxlv = bonus['lvEnd']
        if (level < minlv or level > maxlv) and level != -1:
            continue
        temp = ("等级限制(最低~最高)：%d ~ %d    " % (minlv,maxlv))
        tstr += temp
        if bonus.has_key('itemBonus'):
            itemBonus = bonus['itemBonus']
            name = id.data[itemBonus[0]]['name']
            if id.data[itemBonus[0]].has_key('sexReq'):
                if id.data[itemBonus[0]]['sexReq'] == 1:
                    name += "(性别：男)"
                if id.data[itemBonus[0]]['sexReq'] == 2:
                    name += "(性别：女)"

            bind = bindType[id.data[itemBonus[0]]['bindType']]
            # name = name.encode("utf-8","ignore")
            tid = itemBonus[0]
            limit = checkLimit(0,tid)
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
            temp = ("物品名称：%s    绑定类型：%s    投放限制：%s    " % (name,bind,limit))
            tstr += temp
        if bonus.has_key('bonusSets') and bonus.has_key('itemBonus'):
            tstr += '\n\n'
        if bonus.has_key('bonusSets'):
            bonusSet = bonus['bonusSets']
            num = 1
            temptype = bonus['calcType']
            for Set in bonusSet:
                temp = "    物品分组表%d —— " % num
                num = num + 1
                tstr += temp
                if temptype == 1:
                    temp = "分配方式：分别计算    "
                if temptype == 2:
                    temp = "分配方式：圆桌分配    "
                tstr += temp
                #bonusnum就是bonusSet的id
                bonusnum = Set[0]
                rate = Set[1]
                temp = "掉落几率(万分率)：%d    \n    " % rate
                tstr += temp
                item = bsd.data[bonusnum]
                for tbonus in item:
                    type = ""
                    t_type = tbonus['bonusType']
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
                    name = id.data[tbonus['bonusId']]['name']
                    if id.data[tbonus['bonusId']].has_key('sexReq'):
                        if id.data[itemBonus[0]]['sexReq'] == 1:
                            name += "(性别：男)"
                        if id.data[itemBonus[0]]['sexReq'] == 2:
                            name += "(性别：女)"
                    bind = bindType[id.data[tbonus['bonusId']]['bindType']]
                    limit = checkLimit(bonusnum,tbonus['bonusId'])
                    # name = name.encode("utf-8","ignore")
                    # tlen = len(name)
                    tid = tbonus["bonusId"]
                    temp = ("    物品ID：%d    " % tid)
                    tstr += temp
                    temp = ("类型：%s    " % type)
                    tstr += temp
                    if tbonus['calcType'] == 1:
                        tstr += "分配方式：圆桌分配    "
                    elif tbonus['calcType'] == 2:
                        tstr += "分配方式：分别计算    "
                    rate = tbonus['bonusRate']
                    temp = ("掉落几率(万分率)：%d    " % (rate))
                    tstr += temp
                    if tbonus.has_key('minBonusFormula') and tbonus.has_key('maxBonusFormula'):
                        lv = easygui.enterbox("请输入等级：","等级输入")
                        minNum = tbonus['minBonusFormula']
                        maxNum = tbonus['maxBonusFormula']
                        while not check(lv):
                            easygui.msgbox("请输入数字！")
                            lv = easygui.enterbox("请输入等级：","等级输入")
                        lv = int(lv)
                        calcmin = eval(minNum)
                        calcmax = eval(maxNum)
                        temp = ("掉落数量(最小~最大)：%s = %d ~ %s = %d    " % (minNum,calcmin,maxNum,calcmax))
                        tstr += temp
                    else:
                        minNum = tbonus['minBonusNum']
                        maxNum = tbonus['maxBonusNum']
                        temp = ("掉落数量(最小~最大)：%d ~ %d    " % (minNum,maxNum))
                        tstr += temp
                    temp = ("物品名称：%s    绑定类型：%s    投放限制：%s\n    " % (name,bind,limit))
                    tstr += temp
                    # if tlen <= 30:
                    #     temp += " " * (30 - tlen)
                temp = "\n——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————\n\n"
                tstr += temp
        ans.append(tstr)
    return ans

def search(input_cid,level):
    box = 0
    if cid.data.has_key(input_cid):
        box = cid.data[input_cid]
    else:
        easygui.msgbox("没有查找到此ID!")
        choose()
        return

    ans = []
    if box.has_key('itemSetInfo'):
        ans.extend(itemSetInfo(box['itemSetInfo'][0],level))

    if box.has_key('itemBoxInfo'):
        ans.extend(itemBoxInfo(box['itemBoxInfo'][0],level))

    if box.has_key('needReMapBonusId'):
        if box['needReMapBonusId']:
            try:
                allBonus = bbmd.data[input_cid]
                for bonus in allBonus:
                    tstr = ""
                    if bonus.has_key('sex'):
                        if bonus['sex'][0] == 1:
                            tstr += "性别：男    "
                        if bonus['sex'][0] == 2:
                            tstr += "性别：女    "

                    if bonus.has_key('school'):
                        tstr += "门派：%s    " % school[bonus['school'][0]]

                    if bonus.has_key('bodyType'):
                        try:
                            tstr += "体形：%d" % bonus['bodyType']
                        except TypeError:
                            pass

                    ans.append(tstr)
                    if bonus.has_key('bonusBoxId'):
                        ans.extend(itemBoxInfo(bonus['bonusBoxId'],level))

            except KeyError:
                easygui.msgbox("特殊宝箱数据内没有此数据！")

    str = ""
    for a in range(0,ans.__len__()):
        # ans[a] = ans[a].encode("utf-8","ignore")
        str += ans[a]+"\n"

    boxname = id.data[input_cid]['name']
    title = "默认全等级结果"
    if level != -1:
        title = "人物为%d级时结果" % level

    if cid.data.has_key(input_cid) and cid.data[input_cid].has_key('useLimit'):
        boxname += "(使用间隔为 %s ,使用次数为 %d 次)" % (limitInterval[cid.data[input_cid]['useLimit'][0][0]],cid.data[input_cid]['useLimit'][0][1])

    easygui.textbox("编号为%d,名字为 %s 的物品宝箱查询到以下结果" % (input_cid,boxname),title,str,codebox=1)
    choose()


def search1(input_cid,level):
    box = 0
    if tbd.data.has_key(input_cid):
        box = tbd.data[input_cid]
    else:
        easygui.msgbox("没有查找到此ID!")
        choose()
        return


    ans = []
    if box.has_key('bonusId'):
        str = "奖励配置_主表(bonus_data):\n"
        ans.append(str)
        item = box['bonusId']
        if not bd.data.has_key(item):
            easygui.msgbox("奖励配置主表找不到对应内容！可能需要重新更新！")
            choose()
            return
        bonus = bd.data[item]
        #根据type来确定类型，1和公共奖励包一样，2和奖励分组一样
        if bonus['type'] == 1:
            tbonus = bonus['bonusIds']
            for bonusId in tbonus:
                ans.extend(itemBoxInfo(bonusId,level))
        if bonus['type'] == 2:
            tbonus = bonus['bonusIds']
            for bonusId in tbonus:
                ans.extend(itemSetInfo(bonusId,level))
        if bonus['type'] == 3:
            tbonus = bonus['fixedBonus']
            minLv = -1
            maxLv = 100
            if tbd.data[input_cid].has_key('needLvRange'):
                minLv = tbd.data[input_cid]['needLvRange'][0]
                maxLv = tbd.data[input_cid]['needLvRange'][1]
            if level < minLv or level > maxLv:
                easygui.msgbox("此人物等级下没有物品！对应等级为%d~%d"%(minLv,maxLv),"异常结果")
                choose()
                return
            for bonusthing in tbonus:
                tstr = "    "
                # 1=物品 2=金钱 3=声望 4=经验 5=钓鱼熟练度 6=社会经验 7=灵识 8=公会贡献
                if bonusthing[0] == 1:
                    tid = bonusthing[1]
                    name = id.data[tid]['name']
                    if id.data[tid].has_key('sexReq'):
                        if id.data[itemBonus[0]]['sexReq'] == 1:
                            name += "(性别：男)"
                        if id.data[itemBonus[0]]['sexReq'] == 2:
                            name += "(性别：女)"
                    bind = bindType[id.data[tid]['bindType']]
                    limit = checkLimit(0,)
                    temp = ("物品ID：%d    " % tid)
                    tstr += temp
                    temp = ("类型：%s    " % "物品")
                    tstr += temp
                    temp = ("掉落数量：%d    " % bonusthing[2])
                    tstr += temp
                    temp = ("物品名称：%s    绑定类型：%s    投放限制：%s" % (name,bind,limit))
                    tstr += temp
                    ans.append(tstr)

                if bonusthing[0] == 2:
                    tid = bonusthing[1]
                    temp = ("物品ID：%d    " % tid)
                    tstr += temp
                    temp = ("类型：%s    " % "金钱")
                    tstr += temp
                    temp = ("掉落数量：%d    " % bonusthing[2])
                    tstr += temp
                    ans.append(tstr)

                if bonusthing[0] == 3:
                    tid = bonusthing[1]
                    temp = ("物品ID：%d    " % tid)
                    tstr += temp
                    temp = ("类型：%s    " % "声望")
                    tstr += temp
                    temp = ("掉落数量：%d    " % bonusthing[2])
                    tstr += temp
                    ans.append(tstr)

                if bonusthing[0] == 4:
                    tid = bonusthing[1]
                    temp = ("物品ID：%d    " % tid)
                    tstr += temp
                    temp = ("类型：%s    " % "经验")
                    tstr += temp
                    temp = ("掉落数量：%d    " % bonusthing[2])
                    tstr += temp
                    ans.append(tstr)

                if bonusthing[0] == 5:
                    tid = bonusthing[1]
                    temp = ("物品ID：%d    " % tid)
                    tstr += temp
                    temp = ("类型：%s    " % "钓鱼熟练度")
                    tstr += temp
                    temp = ("掉落数量：%d    " % bonusthing[2])
                    tstr += temp
                    ans.append(tstr)

                if bonusthing[0] == 6:
                    tid = bonusthing[1]
                    temp = ("物品ID：%d    " % tid)
                    tstr += temp
                    temp = ("类型：%s    " % "社会经验")
                    tstr += temp
                    temp = ("掉落数量：%d    " % bonusthing[2])
                    tstr += temp
                    ans.append(tstr)

                if bonusthing[0] == 7:
                    tid = bonusthing[1]
                    temp = ("物品ID：%d    " % tid)
                    tstr += temp
                    temp = ("类型：%s    " % "灵识")
                    tstr += temp
                    temp = ("掉落数量：%d    " % bonusthing[2])
                    tstr += temp
                    ans.append(tstr)

                if bonusthing[0] == 8:
                    tid = bonusthing[1]
                    temp = ("物品ID：%d    " % tid)
                    tstr += temp
                    temp = ("类型：%s    " % "公会贡献")
                    tstr += temp
                    temp = ("掉落数量：%d    " % bonusthing[2])
                    tstr += temp
                    ans.append(tstr)

        str = ""
        for a in range(0,ans.__len__()):
            # ans[a] = ans[a].encode("utf-8","ignore")
            str += ans[a]+"\n"

        boxname = tbd.data[input_cid]['name']
        title = "默认全等级结果"
        if level != -1:
            title = "人物为%d级时结果" % level

        if cid.data.has_key(input_cid) and cid.data[input_cid].has_key('useLimit'):
            boxname += "(使用间隔为 %s ,使用次数为 %d 次)" % (limitInterval[cid.data[input_cid]['useLimit'][0][0]],cid.data[input_cid]['useLimit'][0][1])

        easygui.textbox("编号为%d,名字为 %s 的可交互宝箱查询到以下结果" % (input_cid,boxname),title,str,codebox=1)
        choose()

    else:
        name = ""
        if tbd.data[input_cid].has_key('name'):
            name = tbd.data[input_cid]['name']
        easygui.msgbox("名称为 " + name + " 的宝箱没有掉落物品！")
        choose()
        return


def check(str):
    if re.match('^[0-9]+$',str):
        return True
    else:
        return False

def mainsearch():
    a = easygui.multenterbox("请在下面输入你要查找的信息，等级可不填，不填默认全等级","物品宝箱查找",("宝箱ID：","人物等级："))
    if a == None:
        return
    if check(a[0]) and a[0] != "":
        if check(a[1]) and a[1] != "":
            search(int(a[0]),int(a[1]))
        else:
            search(int(a[0]),-1)
    else:
        easygui.msgbox("请输入数字！")
        mainsearch()

def mainsearch1():
    a = easygui.multenterbox("请在下面输入你要查找的信息，等级可不填，不填默认全等级","可交互宝箱查找",("宝箱ID：","人物等级："))
    if a == None:
        return
    if check(a[0]) and a[0] != "":
        if check(a[1]) and a[1] != "":
            search1(int(a[0]),int(a[1]))
        else:
            search1(int(a[0]),-1)
    else:
        easygui.msgbox("请输入数字！")
        mainsearch1()


def choose():
    temp = easygui.ynbox("请选择要查找的宝箱类型！",
                  "宝箱类型选择",
                  choices=("[<F1>]物品宝箱", "[<F2>]可交互宝箱"),
                  image=None,
                  default_choice='[<F1>]物品宝箱',
                  cancel_choice='[<F2>]可交互宝箱')

    if temp:
        mainsearch()
    else:
        mainsearch1()


if __name__ == '__main__':
    init()
    choose()
    # mainsearch()



