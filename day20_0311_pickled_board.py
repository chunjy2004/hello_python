""" '피클'드 게시판 글쓰기
  - pickle.load(f) : 객체(f)를 읽어서 올린다.
  - pickle.dump(data, f) : 객체(f)에 데이터(data)를 덤프한다.
  - week_num = datetime.date(2018, 06, 12).weekday() : 요일
 """
import time
import datetime
import pickle
import os

import _script_run_utf8
_script_run_utf8.main()

FILENAME_WITH_DIR = "./_static/_pickle/pickled_board.pck"

def write_pickle(filename_with_dir, data):
    with open(filename_with_dir, 'wb') as f:
        pickle.dump(data, f)

def get_read_pickle(filename_with_dir):
    with open(filename_with_dir, 'rb') as f:
        return pickle.load(f)

BOARD_DICT = get_read_pickle(FILENAME_WITH_DIR)

def show_board_list(board_dict):
    print("총 데이터: ('%s건')"% len(board_dict))
    print("------------------------------------------------")
    print("번호....날짜......[제.....목].................")
    print("------------------------------------------------")

    for i, key in enumerate(board_dict, 1):
        title = board_dict[key].split('\n')[0]
        print("%s. [%s] - %s"% (
            i,
            key, title,
        ))
    print("------------------------------------------------")
    print(":입력 키값: (V)eiw / (A)dd / (Q)uit")

def show_detail_view(board_dict, key):
    key = 20180308
    key_str = str(key)
    year, month, day = key_str[:4], key_str[4:6], key_str[6:]
    title = board_dict[key].split('\n')[0]
    content = board_dict[key].replace( title+'\n', '')

    print("%s (%s.%s.%s)" % (title, year, month, day))
    print("-----------------------------------------------")
    print("%s"% content)
    print("-----------------------------------------------")
    input("돌아가기 = 엔터")
    os.system('cls')
    show_board_list(board_dict)

while True:
    show_board_list(BOARD_DICT)

    order = input('명령을 입력하세요 v_날짜형식')

    if order[0].upper().startswith('V'):
        key = int(order.split('_')[1])
        show_detail_view(BOARD_DICT, key)

    elif order[0].upper().startswith('D'):
        pass

    elif order[0].upper().startswith('A'):
        pass

    elif order[0].upper().startswith('Q'):
        aldfjkajljajaklal

    else:
        print('.. 명령어를 이해하지 못했습니다 ..')
"""
    중복데이터 : ('5건')
    ----------------------------------------------
    번호....날짜......[제.....목]...............
    ----------------------------------------------
    1. [10000101] - (예시)제목/내용
    2. [20000101] - (예시) 제목/내용
    3. [20180303] - 축구시즌이 시작되었습니다.
    4. [20180305] - 일기장 마무리 되어감
    5. [20180307] - 아.. 헷갈린다
    6. [20180308] - '피클'데이터는 수정불가
    ----------------------------------------------
    :입력 키값: (V)eiw / (A)dd / (Q)uit
"""
