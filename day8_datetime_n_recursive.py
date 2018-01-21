import os
import time
import datetime
def test_1_datetime_module():
    while True:
        _time = datetime.datetime.now()

        ampm = _time.strftime('%p')
        hour = _time.strftime('%H')
        minute = _time.strftime('%M')
        second = _time.strftime('%S')
        weekday = _time.strftime('%a')

        print(ampm + ' ' + hour + ' : ' + minute + ' : ' + second + ' - ' + weekday)
        _time_format = _time.strftime('%p %H:%M:%S - %A %B %d' )
        print(_time_format)
        time.sleep(1)
        os.system('cls')
# test_1_datetime_module()

for n in range(10, -1, -1):
    print(n)
    time.sleep(0.2)


def countdown(start_number):
    number = -1

    if number <= 0:
        print('fire!')
    else:
        print(number)
        time.sleep(0.2)
        countdown(number-1)

def get_factorial(number):
    _a = get_factorial(2)
    print(_a)



def show_factorial(number):
    _equation = str(number)
    _value = get_factorial(number)
    for i in range(number-1, -1)

if number != 1:
    return number * get_factorial(number-1)
else:
    return 1


def get_fibonacci(times):
    if times > 1:
        a, b = 0,1
        for n in range(times-1):
            a, b = b, a + b
        return b

elif times <= 1:
    return times

_a =







import sys
import turtle

def wait_esc():
    input("Enter to esc ------>\n\n")

turtle.forward(100)
wait_esc


turtle.forward(100)
turtle.left(90)

turtle.forward(100)
turtle.left(90)

turtle.forward(100)
turtle.left(90)

turtle.forward(100)
turtle.left(90)

turtle.mainloop()
