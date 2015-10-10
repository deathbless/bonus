#coding=utf-8
import os
import easygui
import codecs

def convertEncoding(from_encode,to_encode,old_filepath):
    f1=file(old_filepath)
    content2=[]
    while True:
        line=f1.readline()
        content2.append(line.decode(from_encode).encode(to_encode))
        if len(line) ==0:
            break

    f1.close()
    f2=file(old_filepath,'w')
    f2.writelines(content2)
    f2.close()

def convertFromGBK2utf8(filepath):
    convertEncoding("GBK","UTF-8",filepath)

def dellast(filename):
    convertFromGBK2utf8(filename)
    f = open(filename,"r")
    a = ["#coding=utf-8"]
    t = f.readline()
    while t:
        a.append(t)
        t = f.readline()
    print filename,
    del a[1]
    a.pop()
    a.pop()
    f.close()
    # f = codecs.open(filename,"w",'utf-8')
    f = open(filename,"w")
    for t in a:
        f.write(t)
    f.close()

if __name__ == '__main__':
    choices = {'01.孟刚':1,
               '02.丰羽':2,
               '03.锦河':3,
               '04.陈炜':4,
               '05.阮洋':5,
               '06.小勤':6,
               '07.公共':7,
               '08.潘潘':8,
               '09.连长':9,
               '10.小强':10,
               '11.余飞':11,
               '12.丝丝':12,
               '13.格子':13,
               '14.周唯':14,
               '15.沈宇杰':15,
               '16.余辰侃':16,
               '17.文案':17,}
    t = easygui.choicebox("请选择要更新的私服:","更新",choices=choices.keys())
    if t == False:
        exit()
    num = choices[t.encode("UTF-8")]
    os.chdir("data")
    os.system("update.bat " + str(num))
    dellast("bonus_box_data.py")
    dellast("fame_data.py")
    dellast("bonus_set_data.py")
    dellast("consumable_item_data.py")
    dellast("item_data.py")
    dellast("treasure_box_data.py")
    dellast("bonus_data.py")
    dellast("box_bonus_map_data.py")
    dellast("game_item_limit_data.py")
    easygui.msgbox("更新完成！","更新")