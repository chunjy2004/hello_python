import _script_run_utf8
_script_run_utf8.main()

test_text = """
 2
 e
 이
yee
이꾸요잇"""

test2_text = "숫자 2\n" +\
            "영어 e\n" +\
            "마스터 이\n" +\
            "yee\n" +\
            "이꾸요잇\n"


print(test_text)
print(test2_text)

def write():
    # f = open('./_static/_pdb/day18-1_text.pdb', 'w', encoding='utf8')
    # f.write(test_text)
    # f.close
    with open('./_static/_pdb/day18-1_text.pdb', 'w', encoding='utf8') as f:
        f.write(test_text)

    with open('./_static/_pdb/day18-1_text.pdb', 'a', encoding='utf8') as f:
        f.write(test2_text)

write()
