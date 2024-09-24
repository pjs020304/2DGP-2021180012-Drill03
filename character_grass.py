from pico2d import *
import math
open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

def run_rectangle():
    print('RECTANGLE')
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
    break
    
close_canvas()
