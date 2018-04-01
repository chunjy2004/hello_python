# 1번째
import _static.module_custom.class_car as cc

a = cc.SportCar('PORSCHE')
print(a.show_status())
a.speed_up_down(a)


# 2번째
from _static.module_custom.class_car import *


if __name__ == '__main__':
    a = TruckCar('T')
    b = TruckCar('BONGO')
    c = SportCar('PORSCHE')

    # 나(self) 만 바꿀 수 있다
    c.attr['max_speed'] = 200
    c.attr['s_able'] = 50

# 3번쨰
c.show_status()

speed_up_down(c)
speed_up_down(b)

from _static.module_custom.class_car import SportCar, speed_up_down
a = SportCar('PORSCHE')
print(a.show_status())
speed_up_down(a)
