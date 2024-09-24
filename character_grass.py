from pico2d import *

open_canvas()

def run_rectangle():
    print('RECTANGLE')
    pass
def run_circle():
    print('CIRCLE')
    pass

grass = load_image('grass.png')
boy = load_image('character.png')

while True:
    run_circle()
    run_rectangle()
    
close_canvas()
