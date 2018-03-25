SEPERATOR = '\n' + '__'*20 + '\n\n\n'
def test1():
    while True:
        _a_str = input('input a string = ')
        _b_str = input('input b string = ')

        try:
            _c = int(_a_str) / int(_b_str)
        except:
            print(SEPERATOR)
            continue

        print('%s / %s = %s' %(_a_str, _b_str,_c), end='\n\n\n')
        # print('{:,}' X '{:,}' = '{:,}'.format(str(_a_str), str(_b_str), str(_c)), end='\n\n\n')





def test2_when_input_integer():
    while True:
        try:
            _a_int = int(input('input a integer ='))
            _b_int = int(input('input b integer ='))
        except ValueError:
            print('Input number only \n\n')
            continue
        print('SEE ME? O.K..!!\n\n')

        try:
            _answer = _a_int / _b_int
        except ZeroDivisionError:
            print('Cannot divide zero', SEPARATOR)
            continue

        except:
            pass

        else:
            pass

        finally:
            pass

        print('%s / %s = %s' %(_a_int, _b_int, _answer), SEPARATOR)
# test2_when_input_integer()








NATO_PHONETIC_ALPH = """
    A	Alfa
    B	Bravo
    C	Charlie
    D	Delta
    E	Echo
    F	Foxtrot
    G	Golf
    H	Hotel
    I	India
    J	Juliett
    K	Kilo
    L	Lima
    M	Mike
    N	November
    O	Oscar
    P	Papa
    Q	Quebec
    R	Romeo
    S	Sierra
    T	Tango
    U	Uniform
    V	Victor
    W	Whiskey
    X	X-ray
    Y	Yankee
    Z	Zulu
    -	Dash
    """












def nato_phonetic():
    """ GOOGLE = nato phonetic alphabet table python
      refer to : http://www.101computing.net/nato-phonetic-alphabet/
      Did You Know?

      The NATO Phonetic Alphabet is the most widely used spelling alphabet.
      A spelling alphabet (aka radio alphabet, or telephone alphabet) is a set of
      words used to stand for the letters of an alphabet in oral communication.

      Each word in the spelling alphabet typically replaces the name of the letter
      with which it starts. It is used to spell out words when speaking to someone
      not able to see the speaker, or when the audio channel is not clear.
     """

    NATO_PHONETIC_ALPH = """
        A	Alfa
        B	Bravo
        C	Charlie
        D	Delta
        E	Echo
        F	Foxtrot
        G	Golf
        H	Hotel
        I	India
        J	Juliett
        K	Kilo
        L	Lima
        M	Mike
        N	November
        O	Oscar
        P	Papa
        Q	Quebec
        R	Romeo
        S	Sierra
        T	Tango
        U	Uniform
        V	Victor
        W	Whiskey
        X	X-ray
        Y	Yankee
        Z	Zulu
        -	Dash
        """
    TITLE ="""
    \t __________________________________________
    \t   *** NATO PHONETIC ALPHABET ENCODING ***
    \t ------------------------------------------
    \t    - 2017.10.8 -  made by : %s
    \t __________________________________________\n\n\n"""

    def show_title():
        print(TITLE % '!Kay SuparX!')

    def get_code_from_NPA(str_code):    # input 'str' -> output 'dict'
        arr_line = str_code.strip().split("\n")
        dict_code = {}

        for arr_word in arr_line:      #27
            b = arr_word.strip().split()
            dict_code[b[0]] = b[1]

        return dict_code                # <class 'dict'>

    def input_phrase():                 # return CHKD_word...
        print("__"*30)
        str_word = input('TYPE YOUR WORD: ')
        print(".."*30)

        arr_word = str_word.strip().split()
        chkd_word = ""

        for word in arr_word:
            if word.isalpha() == True:
                chkd_word = chkd_word + word.upper() + " "
            else:
                if word.count('-'):
                    chkd_word = chkd_word + word.upper() + " "
                else:
                    print("\n\n\n.. WRONG LETTERS ... TRY AGAIN~!!!! \n SYSTEM TERMINATED~!! ")
                    chkd_word = ""
                    break
        return chkd_word                            # <class 'str'>

    def get_NPA_encode(normal_word, dict_code):     # input = srt, dict
        NPA_encode_word = ""
        # print("normal_word =", normal_word)
        for letter in normal_word:
            if letter != " ":
                NPA_encode_word = NPA_encode_word + "%s = %s" %(letter, dict_code[letter]) + "\n"
            else:
                NPA_encode_word = NPA_encode_word + "\n"
        return NPA_encode_word                              # <class 'str'>

    def main():
        dict_code = get_code_from_NPA(NATO_PHONETIC_ALPH)   # <class 'dict'>
        chkd_word = input_phrase()                          # <class 'str'>

        # print(type(chkd_word))
        print('ORIGINAL WORD = ',chkd_word)   # <class 'str'>
        print()

        NPA_encode_word = get_NPA_encode(chkd_word, dict_code)
        print(NPA_encode_word)



    show_title()

    while True:
        main()





RUN_IMAGE = [
 '''
 .ooooo.
 oo..oo.
 oo..oo.
 oo..oo.
 ooooo..''',
 '''
 ..oo...
 oooo...
 ..oo...
 ..oo...
 oooooo.''',
 '''
 .ooooo.
 o...oo.
 ..ooo..
 ooo....
 oooooo.''',
 '''
 .ooooo.
 ....oo.
 .oooo..
 ...ooo.
 ooooo..''',
 '''
 ...oo..
 .oo.o..
 oo..o..
 oooooo.
 ....o..''',
 '''
 .ooooo.
 oo.....
 oooooo.
 ....oo.
 ooooo..''',
 '''
 .ooooo.
 oo.....
 oooooo.
 oo..oo.
 .oooo..''',
 '''
 oooooo.
 o...oo.
 ...oo..
 ..oo...
 .oo....''',
 '''
 .ooooo.
 oo..oo.
 .oooo..
 oo..oo.
 .oooo..''',
 '''
 .ooooo.
 oo...o.
 oooooo.
 ....oo.
 ooooo..''',
 ]

import os
import time

for n in range(9,-1,-1):
    print('\n\n\n\n\n\n\n')
    print(RUN_IMAGE[n].replace('o','■').replace('.', '∴'))
    time.sleep(1.0)
    os.system('cls')




def test6():
    _a = '''
     .ooooo.
     oo...o.
     oooooo.
     ....oo.
     ooooo..''',

    _b = '''
     .ooooo.
     oo..oo.
     oo..oo.
     oo..oo.
     ooooo..''',

    _a_arr = _a.strip().split('\n')
    _b_arr = _b.strip().split('\n')

    _c_arr = []
    for n in range(5):
        if n == 0:
            _c_arr.append(' '+_a_arr[n]+' '+_b_arr[n])
        else:
            _c_arr.append(_a_arr[n]+_b_arr[n])

    print(_c_arr)

    print('\n\n\n\n')
    for n in range(5):
        print(_c_arr[n])
