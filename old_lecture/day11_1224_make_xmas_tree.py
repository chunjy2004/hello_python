from making_thing.tree_ornament import *


def star(pos_x, pos_y, size=10, width=3):
    tu.color('red','yellow')
    move(pos_x, pos_y)
    tu.width(width)
    tu.begin_fill()
    tu.left(90+126)
    for i in range(5):
        tu.forward(size)
        tu.right(144)
        tu.forward(size)
        tu.left(72)
    tu.end_fill()
    tu.setheading(0)

def tree_trunk(pos_x, pos_y, forward, width=10):
    tu.setheading(0)
    tu.setpos(pos_x, pos_y)
    tu.width(width)
    tu.pencolor('brown')
    tu.right(90)
    tu.forward(forward)
    tu.setheading(0)

def draw_triangle(pos_x, pos_y, lowerside, width=5, angle=40):
    l = lowerside / 2
    radian = math.radians(angle)
    sameside = l/math.cos(radian)

    tu.color('darkgreen', 'green')
    tu.width(width)
    move(pos_x, pos_y)

    tu.begin_fill()
    tu.right(angle)
    tu.forward(sameside)
    tu.left(180+angle)
    tu.forward(lowerside)
    tu.left(180+angle)
    tu.forward(sameside)
    tu.right(angle)
    tu.end_fill()

def main():
    star(0, 330, 40, 10)
    tree_trunk(0, 260, 620, 40)

    draw_triangle(0, 300, 250)
    draw_triangle(0, 230, 350)
    draw_triangle(0, 120, 500)
    draw_triangle(0, 0, 650)

    pos_x = [330, 250, 180, 125,
        -330, -250, -180, -125,
        -59, -68, -104, -106,
        ]

    pos_y = [-330, -150, 20, 140,
        -330, -150, 20, 140,
        -13, -60, -126, -127,
        ]
    pos_xy = list(zip(pos_x, pos_y))

    for posxy in pos_xy:
        fill = random.choice(COLOR_PICK)
        draw_color_bulb(posxy[0], posxy[1], 20, 5, 'red', fill=fill)

if __name__ == '__main__':
    main()
    move(0, -230)
    tu.write("MERRY CHRISTMAS\n & HAPPY NEW YEAR!",
        font=("arial", 30, 'bold'),
        align='center')
    def show_cord(x,y):
        print('(%s, %s)'% (x, y))

    tu.onscreenclick(show_cord)
    tu.mainloop()

#     while True:
#         for n in range(random.randint(5,20)):
#             posy = random.randint(-250, 250)
#             posx = random.choice([-1,1])*0.3*(500-posy)/random.randint(1,4)
#             # posy = random.randint(-300, 300)
#             # posx = random.randint(-450, 450)
#             size = random.randint(10, 20)
#             width = 3
#             pen = random.choice(COLOR_PICK)
#             fill = random.choice(COLOR_PICK)
#
#             draw_color_bulb(posx, posy, size=size, width=width, pen=pen, fill=fill)
#             print('%s , %s' %(posx, posy))
#         time.sleep(0.1)

tu.mainloop()
