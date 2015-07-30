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
    t = easygui.ynbox("请问是否更新！","更新")
    if t == False:
        exit()
    os.chdir("data")
    os.system("update.bat")
    dellast("bonus_box_data.py")
    dellast("fame_data.py")
    dellast("bonus_set_data.py")
    dellast("consumable_item_data.py")
    dellast("item_data.py")
    easygui.msgbox("更新完成！","更新")