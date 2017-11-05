def test1():
    _a = 100
    _b = 3

    _c = _a + _b # = 103

    _d = _a / _b
    _e = _a // _b
    _f = _a % _b

    print(_d) # = 33.33333333.... 'float' = 'int' / 'int'
    print(_e) # = 33 'int'
    print(_f) # = 1 'int'
# test1()
def test2():
    _a = """\tdladkfjla\n\tdafadf\n\tadsfas"""
    print(_a)

    _a = "python's favorite food is perl"
    _a = 'python\'s \\favorite food is perl\a'
    print(_a)

    _a = "this"
    _b = " is book"

    _c = (_a + _b + '\n')*5
    print(_c)
# test2()
def test3():
    _a = "Life is too short, you need Python"
    print(_a[-1:-6])
# test3()
def test4():
    pass

import random

_a = ['I', 'You', 'He', 'She', 'Dog']
_b = ['spit', 'ate', 'trashed', 'throw', 'danced with']
_c = ['1','2','3','4','5','6']
_d = ['banana', 'pear', 'yaloli', 'peach', 'Earth', 'park geun hea', 'computer', 'dollar']

_a_num = len(_a)
_b_num = len(_b)
_c_num = len(_c)
_d_num = len(_d)

for n in range(10):
    _a_rand_num = random.randint(1, _a_num)
    _b_rand_num = random.randint(1, _b_num)
    _c_rand_num = random.randint(1, _c_num)
    _d_rand_num = random.randint(1, _d_num)

    # print('%s ate %s %s'%(_a, _b, _c))
    print('%s %s %s %s'%(
    _a[_a_rand_num-1], _b[_b_rand_num-1], _c[_c_rand_num-1], _d[_d_rand_num-1]))
