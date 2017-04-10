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

player = gamebox.from_color(400, 0, 'yellow', 20, 40)
platforms[1].x = 400

def tick(keys):
    camera.clear('cyan')

    # move platforms down
    for platform in platforms:
        platform.y += 3
        if platform.top > camera.bottom + 20:
            platform.y = -50
            platform.x = random.randrange(0, 800)
            platform.size = random.randrange(100, 500), 20


    # player horizontal motion
    if pygame.K_RIGHT in keys:
        player.x += 10
    if pygame.K_LEFT in keys:
        player.x -= 10

    # player gravity
    player.speedy += 0.5
    player.move_speed()

    can_jump = False
    # player bumps into stuff
    for platform in platforms:
        if player.touches(platform):
            player.move_to_stop_overlapping(platform)
            if player.bottom_touches(platform):
                can_jump = True
                player.speedy = 3

    # player jump
    if can_jump and pygame.K_SPACE in keys:
        player.speedy = -10


    for platform in platforms:
        camera.draw(platform)
    camera.draw(player)


    camera.display()

ticks_per_second = 30

gamebox.timer_loop(ticks_per_second, tick)

