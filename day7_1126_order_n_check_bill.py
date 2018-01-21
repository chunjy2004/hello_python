#! python
import os
import sys
import datetime
""" file-docs : OPEN A RESTAURANT : Making Order System
  (1) to Show MENU_PAN = MENU_PAN (changeable)
  (2) to Input order = by Item index & quantity
  (3) to Calculate the Bills = Including (Tax= 6.5%, Tip= 10%)

 * Release Note : correct sorting version
    - Dict can not be ordered / arrange 'list' first.
    - Question : _arr.sort() = None. sorted(_arr) = 'list' O.K
    - I don't know the differences btw .sort() & sorted()
"""
SEPARATOR = '__'*22
MENU_DICT = {
    1 : ['BlACK_NOODLE', 5500],
    2 : ['RED_NOODLE', 6500],
    3 : ['ROLLED_RICE', 3500],
    4 : ['TTUK-BOK-KI', 3500],
    5 : ['FRIED_DUMPLINGS', 3000],
    6 : ['SPRITE(7-UP)', 1000],
    7 : ['BOTTLED_WATER', 500],}
MENU_PAN_FORMAT = ""                                +\
    "-------------------------------------------\n" +\
    "     MENU-PAN  / Onito's Restautant        \n" +\
    "-------------------------------------------\n" +\
    "%s"                                            +\
    "-------------------------------------------\n"
BILL_FORMAT = ""                                    +\
    "-------------------------------------------\n" +\
    "     $$$ BILL / Onito's Restautant $$$     \n" +\
    "-------------------------------------------\n" +\
    "%s"                                            +\
    "-------------------------------------------\n"

def show_menu_pan():
    """ MAKING MENU_PAN of Your RESTAURANT
      - print(MENU_PAN_FORMAT %  MENU_STRING)
      - make MENU_STRING from MENU_DICT
    """
    MENU_STRING = ''
    for key in MENU_DICT.keys():            # use .keys() .values() .items()
        MENU_STRING += '{:>2}. {:<16} {:.^10} {:5,} won'.format(
        key,
            MENU_DICT[key][0],
            '.',
            MENU_DICT[key][1]) + '\n'
    print(MENU_PAN_FORMAT %MENU_STRING)


def get_input_str():
    input_message = '' +\
    'please, order menu by index_quantity & space\n' +\
    '(ex: 1-2, 2-3, 3-2...):\n'
    menu_order_str = input(input_message)
    return menu_order_str

show_menu_pan()
menu_order_str = get_input_str()


order_arr = menu_order_str.strip().split()

# print(order_arr[0])
# print(order_arr[1])
# print(order_arr[2])

# _a_arr = order_arr[0].strip().split('-')
# print(_a_arr)

# print(_a_arr[0])
# print(_a_arr[1])

ORDER_DICT = {}

# _key = _a_arr[0]
# _value = _a_arr[1]

# ORDER_DICT[_key] = _value


for order in order_arr:
    _key = int(order.strip().split('-')[0])
    _value = int(order.strip().split('-')[1])
    ORDER_DICT[_key] = _value

_menu_total = 0
for i, key in enumerate(ORDER_DICT.keys(), 1):
    '1. name price amount = all'
    _item = MENU_DICT[key][0]
    _price = MENU_DICT[key][1]
    _quantity = ORDER_DICT[key]
    _total = _price * _quantity
    _menu_total += _total
    print('{:2}. {:<15} {:.^10} {:6,} X {:2} = {:7,}'.format(i, _item, '.',  _price, _quantity, _total))
print(_menu_total)
# print(menu_order_str)
# print(type(menu_order_str))

# menu_order_str = input()
# print(menu_order_str)
# return menu_order_str
# menu_order_str = get_input_str()
