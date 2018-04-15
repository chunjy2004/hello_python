from game_character import Character

class Monster(Character):
    _total_count = 0

    def __init__(self):
        super().__init__()
        Monster._total_count += 1

class Ghoul(Monster):
    _total_count = 0

    def __init__(self):
        super().__init__()
        Ghoul._total_count += 1
        print("%s 생성되었습니다."% self.__class__.__name__)

class Dragon(Monster):
    _total_count = 0

    def __init__(self):
        super().__init__()
        Dragon._total_count += 1
        print("%s 생성되었습니다."% self.__class__.__name__)


if __name__ == '__main__':
    a = Monster()
    b = Monster()

    print("캐릭터의 개수=", Character._total_count)
    print("몬스터의 개수=", Monster._total_count)
    print("용의 개수=", Dragon._total_count)
    print("구울의 개수=", Ghoul._total_count)
