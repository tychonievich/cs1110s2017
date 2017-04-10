import pygame
import gamebox
camera = gamebox.Camera(800,600)

frame = 0
b1 = gamebox.from_color(50, 100, "red", 20, 40)

def tick(keys):
    global frame
    frame += 1

    camera.clear('black')

    camera.draw(b1)
    if pygame.K_RIGHT in keys:
        b1.x += 5
    if pygame.K_LEFT in keys:
        b1.x -= 5
    if pygame.K_UP in keys:
        b1.y -= 5
    if pygame.K_DOWN in keys:
        b1.y += 5

    # usually camera.display() should be the last line of the tick method
    camera.display()

ticks_per_second = 30

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)

