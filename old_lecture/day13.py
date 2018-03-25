
def test1():
    while True:
        _a = int(input('근무 시간을 입력하시오 : '))
        _b = int(input('시간당 수당을 입력하시오 : '))

        if _a > 12:
            _plus = (12*_b)+((_a-12)*_b/100*130)
            print('총 급여는',_plus, '원 입니다.')

            if _a <= 12:
                _money = _a*_b
                print('총 급여는', _money, '원 입니다.')

        _answer = input('다시?(y/n) : ')
        if _answer == 'n':
            break

def test2():

    # _a = 10
    while True:
        _a = int(input('정수를 입력하시오 : '))
        for n in range(1,_a+1):
            if _a%n == 0:
                print(n)
        _answer = input('다시?(y/n) : ')
        if _answer == 'n':
            break



_a = input('정수를 입력하시오 : ')

_max = _a
for n in range(1,5):
    _temp = input('정수를 입력하시오 : ')
    if _temp>_max:
        _max = _temp

print('가장 큰 값 :', _max)
