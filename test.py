__author__ = 'hzsunyuda'

import anydbm


def addData(name="",tool=""):
    try:
        db = anydbm.open("db.dat",'c')
        if tool+'all' not in db.keys():
            db[tool+'all'] = '0'
        db[tool+'all'] = str(int(db[tool+'all']) + 1)
        if tool+name not in db.keys():
            db[tool+name] = '0'
        db[tool+name] = str(int(db[tool+name]) + 1)

    finally:
        db.close()

def loadData(name="",tool=""):
    db = anydbm.open('db.dat', 'r')
    if not name:
        return db[tool+'all']
    else:
        if name not in db.keys():
            return '0'
        else:
            return db[tool+name]


def add(a):
    return a+1

if __name__ == '__main__':
    a = {1:1,2:2}
    print filter(add,a)
    print a
