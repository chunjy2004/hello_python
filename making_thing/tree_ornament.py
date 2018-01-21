import random
import turtle as tu
import time
import math


COLOR_PICK = ['red', 'green', 'yellow', 'blue', 'orange', 'violet', 'purple']


tu.speed(0)
tu.screensize(500, 900)

def move(pos_x=0, pos_y=0):
    tu.penup()
    tu.setpos(pos_x, pos_y)
    tu.pendown()

def go(go, angle=0):
    tu.forward(go)
    tu.right(angle)

def draw_color_bulb(pos_x, pos_y, size=10, width=3, pen='red', fill='yellow'):
    move(pos_x, pos_y+size/2)
    tu.width(width)
    tu.color(pen, fill)
    tu.begin_fill()
    tu.circle(size)
    tu.end_fill()


if __name__ == '__main__':
    while True:
        for n in range(random.randint(5,20)):
            # posy = random.randint(-250, 450)
            # posx = random.choice([-1,1])*0.3*(500-posy)/random.randint(1,4)
            posy = random.randint(-300, 300)
            posx = random.randint(-450, 450)
            size = random.randint(10, 20)
            width = 3
            pen = random.choice(COLOR_PICK)
            fill = random.choice(COLOR_PICK)

            draw_color_bulb(posx, posy, size=size, width=width, pen=pen, fill=fill)
            print('%s , %s' %(posx, posy))
        time.sleep(0.1)
