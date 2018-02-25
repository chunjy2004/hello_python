FILE_DIR = './_static/_pdb/'
FILE_NAME = 'test1_file_rw.pdb'
DATA = '안농\n하세\n요'

import _script_run_utf8
_script_run_utf8.main()

def test_write():
    """
    #f = open(FILE_DIR+FILE_NAME, mode='w')
    #f.write(DATA)
    #f.close()
    """

    with open(FILE_DIR+FILE_NAME, mode='w', encoding='utf8')as f:
        f.write(DATA)

def test2_readlines(FILE_NAME):
    f = open(FILE_DIR+FILE_NAME, mode='r', encoding='utf8')
    strings = f.readlines()
    f.close()

    print(strings)
    print('\n\n')

    for string in strings:
        print(string)

def test3_readline(FILE_NAME):
    with open(FILE_DIR+FILE_NAME, mode='r', encoding='utf8')as f:
        string1 = f.readline()
        string2 = f.readline()
        string3 = f.readline()
        for string in [string1, string2, string3]:
            print(string)

    with open(FILE_DIR+FILE_NAME, mode='r', encoding='utf8')as f:
        for line in f:
            print(line)

def test4_read(FILE_NAME):
    with open(FILE_DIR + FILE_NAME, mode='r', encoding='utf8')as f:
        bundle_string = f.read()

    print(bundle_string)



if __name__ == '__main__':
    
    # test3_readline('i_have_a_dream.pdb')
    with open(FILE_DIR+'i_have_a_dream.pdb', mode='r', encoding='utf8')as f:
        strings = f.readlines()

    import time

    for string in strings:
        time.sleep(0.2)
        print(string, flush=True)
