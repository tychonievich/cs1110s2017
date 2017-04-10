import pygame
import gamebox
camera = gamebox.Camera(800,600)

platforms = [
    gamebox.from_color(400, 300, 'black', 400, 20),
    gamebox.from_color(400, 100, 'black', 400, 20),
    gamebox.from_color(400, 200, 'black', 400, 20),
    gamebox.from_color(400, 500, 'black', 400, 20)
]


def tick(keys):
    camera.clear('cyan')
    for platform in platforms:
        camera.draw(platform)
    camera.display()

ticks_per_second = 30

gamebox.timer_loop(ticks_per_second, tick)

