"""
"""
import random


def test1():
    numbers = [n for n in range(1,11)]
    yes5 = ["yes" for n in range(5)]
    yes5_if = ["yes" for n in range(10) if n%2 == 0]
    yes_no_10 = ["yes" if n%2 == 0 else "no" for n in range(1,11)]

    yes_vari = 10 if yes_no_10[0] == "yes" else "what?"

    print(numbers)
    print(yes5)
    print(yes5_if)
    print(yes_no_10)
    print()
    print(yes_vari)

def get_result_of_rock_scissors_paper(me, com):
    """ 가위.바위.보 승무패를 판단해 준다.
    # IN = 1,2,3 중 하나, 가위,바위, 보
    # OUT = 1,0,-1 중 하나 -- 승무패
    """
    eq = me - com
    if eq == 0:
        return -1
    elif eq == 1 or eq == -2:
        return 1
    elif eq == -1 or eq == 2:
        return 0

def is_playing_stop():
    _a_str = input("더 하시겠습니까? (y/n)")
    if _a_str.lower().startswith('n'):
        return True
    else:
        return False

# count = 0
while True:
    me = int(input('me : '))
    com = random.randint(1,3)

    answer = get_result_of_rock_scissors_paper(me, com)        # 블랙박스
    print(answer)

    # count+=1

    # is_playing_stop()
    # print(is_playing_stop)
    stop_ok = is_playing_stop()
    if stop_ok == True:
        break
