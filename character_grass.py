from pico2d import *
import math
open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

def draw_base(cx, cy):
    clear_canvas()
    boy.draw_now(cx,cy)
    grass.draw_now(400,40)
    delay(0.01)

def run_bottom1():
    cx=800//2
    cy=100
    while cx<800:
        draw_base(cx,cy)
        cx+=2

    pass
def run_right():
    cx=800
    cy=100
    while cy<600:
        draw_base(cx,cy)
        cy+=2

    pass
def run_top():
    cx=800
    cy=600
    while cx>0:
        draw_base(cx,cy)
        cx-=2

    pass
def run_left():
    cx=0
    cy=600
    while cy>100:
        draw_base(cx,cy)
        cy-=2

    pass
def run_bottom2():
    cx=0
    cy=100
    while cx<=400:
        draw_base(cx,cy)
        cx+=1
    pass
def run_triright():
    cx=800
    cy=100
    while cy<600:
        draw_base(cx, cy)
        cx -= 4/5
        cy +=1
def run_trileft():
    cx=400
    cy=600
    while cy>100:
        draw_base(cx,cy)
        cx -= 4/5
        cy -=1
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
        x = cx+r*math.cos(math.radians(theta))
        y = cy+r*math.sin(math.radians(theta))
        draw_base(x,y)
    pass
def run_triangle():
    run_bottom1()
    run_triright()
    run_trileft()
    run_bottom2()


while True:
    #run_circle()
    #run_rectangle()
    run_triangle()
    
close_canvas()
