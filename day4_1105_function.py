"""calculator"""

def get_plus_ab(a,b):
    return a + b

def get_minus_ab(a,b):
    return a - b

def get_multi_ab(a,b):
    return a * b

def get_divide_ab(a,b):
    return a / b




while True:
    _qes1 = int(input('a : '))
    _qes2 = int(input('b : '))
    _kind = input('+ / - / X / % : ')
    if  _kind == '+':
        operator = "+"
        c = get_plus_ab(_qes1, _qes2)
        print('\n\t\t%s %s %s = %s'%(_qes1, operator, _qes2, c))
    elif _kind == '-':
        operator = "-"
        c = get_minus_ab(_qes1, _qes2)
        print('\n\t\t%s %s %s = %s'%(_qes1, operator, _qes2, c))
    elif _kind == 'X':
        operator = "X"
        c = get_multi_ab(_qes1, _qes2)
        print('\n\t\t%s %s %s = %s'%(_qes1, operator, _qes2, c))
    elif _kind == '%':
        operator = "%"
        c = get_divide_ab(_qes1, _qes2)
        print('\n\t\t%s %s %s = %s'%(_qes1, operator, _qes2, c))
