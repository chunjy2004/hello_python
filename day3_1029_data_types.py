import random
import time
""" random function drill
(1) random.randint()
(2) random.choice()
(3) random.shuffle()
"""

# print(dir(random))
#
# for n in dir(random)
# print(n)

def test2_randint():
    for n in range(30):
        _a = random.randint(0,10)
        print(_a)

def test3_randchoice():
    pass

def test4_rand_shuffle():
    _a = [0,1,2,3,4,5,6,7,8,9]
    _a = [ n for n in range(10) if n/1 == n ]

    for n in range(10):
        random.shuffle(_a)
        print(_a)

def test5():
    while True:
        _a_str = input('Guess number = ')
        print(_a_str)

        if _a_str == '13':5
            print('Friday the 13th, --- ok out')
            break
        time.sleep(0.3)



INTRODUCE = """
    Your computer has a number one to hundred.

    You have only ten chance to guess.

    Guess the number your computer has..."""

nick = input('Your Name? : ')
print('\n\tWelcome %s..... \n\t%s\n'% (nick, INTRODUCE))
cpu = random.randint(1,100)
while True:
    a = int(input("Guess number what your computer is thinking = "))

    if cpu > a:
        print('\nbigger than you thought')
    elif cpu < a:
        print('\nsmaller than you thought')
    elif cpu == a:
        print("""\nCongradulation, %s! \nThat's what I thought"""% (nick))

        break
