import pygame
import gamebox
camera = gamebox.Camera(800,600)

colors = ['black', 'red', 'green', 'magenta']
frame = 0

def tick(keys):
    global frame
    camera.clear(colors[frame])
    frame += 1
    if frame >= len(colors):
        frame = 0
    # usually camera.display() should be the last line of the tick method
    camera.display()

ticks_per_second = 30

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)

