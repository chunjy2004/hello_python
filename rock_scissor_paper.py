import random

while True:
    if __name__ == '__main__':
        # get_me_com_attacks(length=20)
        attacks = get_me_com_attacks(5)
        # for i in range(len(attacks)):
        #     print(attacks[i])
        for attack in attacks:
            print(attack)
        for attack in attacks:
            result = get_result_rock_paper_scissors(attack)
            print(result)
