from game_character import Character

class Player(Character):
    _total_count = 0

    def __init__(self):
        super().__init__()
        Player._total_count += 1

class Warrior(Player):
    _total_count = 0

    def __init__(self):
        super().__init__()
        Warrior._total_count += 1
        print("%s 생성되었습니다."% self.__class__.__name__)

class Wizard(Player):
    _total_count = 0

    def __init__(self):
        super().__init__()
        Wizard._total_count += 1
        print("%s 생성되었습니다."% self.__class__.__name__)


if __name__ == '__main__':
    a = Warrior()
    b = Wizard()

    print("캐릭터의 개수=", Character._total_count)
    print("몬스터의 개수=", Player._total_count)
    print("용의 개수=", Warrior._total_count)
    print("구울의 개수=", Wizard._total_count)
