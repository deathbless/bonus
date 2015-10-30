#coding=utf-8
__author__ = 'hzsunyuda'
import re
import os
import easygui

import sys
reload(sys)

argv = sys.argv
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
ans = []

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

def check(str):
    if re.match('^[0-9]+$',str):
        return True
    else:
        return False

def itemSetInfo(index,level):
    pass

def itemBoxInfo(index,level):
    pass

def search1(input_cid,level):
    box = 0
    try:
        box = cid.data[input_cid]
    except:
        raise Exception("没有此ID的宝箱")
        return

    if box.has_key('itemSetInfo'):
        itemSetInfo(box['itemSetInfo'][0],level)

    if box.has_key('itemBoxInfo'):
        itemBoxInfo(box['itemBoxInfo'][0],level)



def search2():
    pass

def query(choose,cid,level=0):
    if choose:
        search1(cid,level)
    else:
        search2(cid,level)

if __name__ == '__main__':
    if len(argv) == 3:
        query(argv[0],argv[1],argv[2])
    elif len(argv) == 2:
        query(argv[0],argv[1])
    else:
        exit(1)