from pico2d import *

open_canvas()

def run_rectangle():
    clear_canvas()

def run_circle():
    clear_canvas()


grass = load_image('grass.png')
boy = load_image('character.png')

while True:
    run_rectangle()
    run_circle()
    
close_canvas()
