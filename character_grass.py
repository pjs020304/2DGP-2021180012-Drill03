from pico2d import *
import math
open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')


def run_bottom1():
    cx=800//2
    cy=100
    while cx<800:
        clear_canvas()
        boy.draw_now(cx,cy)
        cx+=2
        grass.draw_now(400, 40)
        delay(0.01)
    pass
def run_right():
    cx=800
    cy=100
    while cy<600:
        clear_canvas()
        boy.draw_now(cx,cy)
        cy+=2
        grass.draw_now(400, 40)
        delay(0.01)
    pass
def run_top():
    cx=800
    cy=600
    while cx>0:
        clear_canvas()
        boy.draw_now(cx,cy)
        cx-=2
        grass.draw_now(400, 40)
        delay(0.01)
    pass
def run_left():
    cx=0
    cy=600
    while cy>100:
        clear_canvas()
        boy.draw_now(cx,cy)
        cy-=2
        grass.draw_now(400, 40)
        delay(0.01)
    pass
def run_bottom2():
    cx=0
    cy=100
    while cx<=400:
        clear_canvas()
        boy.draw_now(cx,cy)
        cx+=1
        grass.draw_now(400, 40)

        delay(0.01)
    pass

def run_rectangle():
    print('RECTANGLE')
    run_bottom1()
    run_right()
    run_top()
    run_left()
    run_bottom2()
    pass
def run_circle():
    print('CIRCLE')
    
    r= 200
    cx = 800/2
    cy = 600/2
    for theta in range(270,630):
        clear_canvas()
        x = cx+r*math.cos(math.radians(theta))
        y = cy+r*math.sin(math.radians(theta))
        boy.draw_now(x,y)
        grass.draw_now(cx, 40)
        delay(0.01)
    pass

while True:
    run_circle()
    run_rectangle()
    
close_canvas()
