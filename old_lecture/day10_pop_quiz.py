
import time
import sys

a = 0
def test1():
    for n in range(10):
      print(a, end=' ', flush=True)
      # sys.stdout.flush()
      a+=1
      time.sleep(0.5)


# print('안녕세계')
# chr(AC00)




# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
# sys.stderr = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

import _script_run_utf8
_script_run_utf8.main()

print('안녕세계')
print(sys.getdefaultencoding())
print(sys.stdout.encoding)
print(sys.stderr.encoding)


_year = '갑을병정무기경신임계'
_number = '4567890123'
_zodiac = '자축인묘진사오미신유술해'

_a = zip(_number, _year)


_a = (lambda x, y: x**2+y**2)(4,3)
print('lambda   = %s'% _a)

def tempo(x,y):
    return(x**2 + y**2)
_b = tempo(4,3)
print('function = %s'%s _b)



def compare_lambda_vs_function(x,y):
    pass
compare_lambda_vs_function(4, 3)
