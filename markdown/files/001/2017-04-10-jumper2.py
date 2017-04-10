import pygame
import gamebox
import random

camera = gamebox.Camera(800,600)

platforms = []
for y in range(0, 600, 100):
    platforms.append(gamebox.from_color(
        random.randrange(0, 800),
        y,
        'black',
        random.randrange(100, 500),
        20))

player = gamebox.from_color(100, 400, 'yellow', 20, 40)

def tick(keys):
    camera.clear('cyan')
    for platform in platforms:
        camera.draw(platform)
    camera.draw(player)
    camera.display()

ticks_per_second = 30

gamebox.timer_loop(ticks_per_second, tick)

