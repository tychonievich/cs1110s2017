import pygame
import gamebox
camera = gamebox.Camera(800,600)

player = gamebox.from_color(50, 100, "red", 20, 40)
obstacle = gamebox.from_color(400, 300, "yellow", 600, 20)


def tick(keys):
    camera.clear('black')

    # move the player
    if pygame.K_RIGHT in keys:
        player.speedx += 0.5
    if pygame.K_LEFT in keys:
        player.speedx -= 0.5
    if pygame.K_UP in keys:
        player.speedy -= 0.5
    if pygame.K_DOWN in keys:
        player.speedy += 0.5

    # gravity
    player.speedy += 0.25

    player.move_speed()


    # handle collisions
    if player.touches(obstacle):
        obstacle.color = 'blue'
        player.move_to_stop_overlapping(obstacle)
    else:
        obstacle.color = 'yellow'

    # draw everything
    camera.draw(player)
    camera.draw(obstacle)

    # usually camera.display() should be the last line of the tick method
    camera.display()

ticks_per_second = 30

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)

