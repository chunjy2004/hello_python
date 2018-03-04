
def test1():
    _n = int(input('1부터 몇까지 더할까요? : '))

    if _n % 2==0:
        print('정답은', (1+_n)*(_n/2), '입니다.')
    elif _n % 2!=0:
        print('정답은', (_n/2*(_n-1))+_n, '입니다.')

import time
import os

f = 10
while True:
    print('|'+'-'*(10-f)+'[HELLO]'+'-'*f+'|'+ 'WORLD')
    time.sleep(0.2)
    os.system('cls')
    f-=1
    if f<0:
        f+=1
        print('|'+'-'*(10-f)+'[HELLO]'+'-'*f+'|'+ 'WORLD')
        time.sleep(0.2)
        os.system('cls')
