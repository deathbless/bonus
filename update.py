import os
os.chdir("data")
os.system("update.bat")

def dellast(filename):
    f = open(filename,"r")
    a = []
    t = f.readline()
    while t:
        a.append(t)
        t = f.readline()
    a.pop()
    a.pop()
    f.close()
    f = open(filename,"w")
    for t in a:
        f.write(t)
    f.close()

dellast("bonus_box_data.py")
dellast("fame_data.py")
dellast("bonus_set_data.py")
dellast("consumable_item_data.py")
dellast("item_data.py")