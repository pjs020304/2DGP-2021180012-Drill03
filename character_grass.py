from pico2d import *

open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

def run_rectangle():
    print('RECTANGLE')
    pass
def run_circle():
    print('CIRCLE')
    clear_canvas()
    boy.draw_now(400,300)
    grass.draw_now(400, 80)
    delay(1)
    pass

while True:
    run_circle()
    run_rectangle()
    break
    
close_canvas()
