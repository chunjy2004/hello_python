
def test1():
    input_score = """
    입력받은 성적
    """

    seperator = '-'*10

    _a = int(input('국어 성적을 입력하세요 : '))
    _b = int(input('수학 성적을 입력하세요 : '))
    _c = int(input('영어 성적을 입력하세요 : '))

    average = (_a+_b+_c)/3

    print(input_score)
    print(seperator)
    print('국어 성적 :',_a)
    print('수학 성적 :',_b)
    print('영어 성적 :',_c,'\n')
    print(seperator,'\n')
    print('총합 :', _a+_b+_c)
    print('평균 :', '%0.2f' % average)

def test2():
    pi = 3.141592

    _r = int(input('반지름을 입력하시오 : '))

    _s = _r*_r*pi
    _f = _r*2*pi

    print('반지름 :', _r)
    print('원의 넓이 :', '%.3f' % _s)
    print('원의 둘레 :', '%0.3f' % _f)

def test3():
    _a = int(input('다섯 자리 숫자를 입력하시오 : '))
    first = (_a//10000)
    second = (_a//1000)%10
    third = (_a//100)%10
    forth = (_a//10)%10
    fifth = (_a%10)
    print(first,',', second,',', third,',', forth,',', fifth)
