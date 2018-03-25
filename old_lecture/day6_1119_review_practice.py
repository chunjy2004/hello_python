
def test1():
    SEPERATOR = '\n' + "__"*30 + '\n'


    print("a =", ord("a"))
    print("A =", ord("A"), SEPERATOR)


    print(chr(97))
    print(chr(65))

def asc_cord_chart():
    counter = 0
    for n in range(1, 128):
        counter+=1
        if counter == 5:
            print(('%s=%s' %(n, chr(n))),'\t\t', end = '\n')
            counter = 0
        else:
            print(('%s=%s' %(n, chr(n))),'\t\t', end = '')
            # if n == 9:
            #아직#연구중#9번째_아즈키코드#삭--제


SEPERATOR = '\n' + "__"*30 + '\n'
MENU_DICT = {
1 : ['black noodle', 5500],
2 : ['red noodle', 8000],
3 : ['tangsuyuk', 10000],
4 : ['sprite', 1500],
}
MENU_FORMAT = """
----------------------------------------
DRAGONCHICKEN'S RESTARAUNT / MENU
----------------------------------------

----------------------------------------"""

print(SEPERATOR)
print("""DRAGONCHICKEN'S RESTAURANT / MENU""")
print(SEPERATOR)
for n in range(0,4):
    # print('%s. %-15s.... %7s won'%(n+1, MENU_DICT[n+1][0], MENU_DICT[n+1][1]))
    print('{}. {:<15}.... {:7,} won'.format(n+1, MENU_DICT[n+1][0], MENU_DICT[n+1][1]))
print(SEPERATOR)
