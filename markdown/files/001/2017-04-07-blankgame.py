# Blank game template - Use this as a blank file to start your game.

import pygame
import gamebox
camera = gamebox.Camera(800,600)

def tick(keys):
    # to check if a key is pressed do, e.g., if pygame.K_LEFT in keys
    # to check the mouse, use camera.mouse (for position) or camera.mouseclick (for buttons)

    # typically here you update the position of the characters
    # then you call camera.draw(box) for each GameBox you made

    # usually camera.display() should be the last line of the tick method
    camera.display()

ticks_per_second = 30

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)

