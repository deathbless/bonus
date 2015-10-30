__author__ = 'hzsunyuda'

def add(a):
    a.append(2)
    raise KeyError
    return 1

if __name__ == '__main__':
    a = [1]
    b = {'a':1}
    if b.has_key('b') and b['b'] == 1:
        print "hello"

