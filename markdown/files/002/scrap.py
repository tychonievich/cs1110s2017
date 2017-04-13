import pygame
import gamebox
import random
camera = gamebox.Camera(800, 600)
character = gamebox.from_color(camera.x, camera.y, 'red', 20, 40)
time = 9000
walls = [
    gamebox.from_color(400, 600, 'black', 802, 100)
]
character.yspeed = 0
# randomize our coins within the list
# rather than coins that sit still, let's make coins that fall towards the character
coins = [
    gamebox.from_color(random.randint(50, 750), -10, 'yellow', 12, 12)
]
# add more platforms, randomly generated
platforms = []
for y in range(0, 600, 150):
    platforms.append(gamebox.from_color(random.randrange(0, 800), y, 'black', random.randrange(100, 500), 20))
score = 0
for coin in coins:
    coin.yspeed = 0
def tick(keys):
    global time
    global score
    camera.clear("blue")
    time -= 1
    # when I want to see the time run out, I just change this to 100
    frac = str(int((time%ticks_per_second)/ticks_per_second*10))
    sec = str(int((time/ticks_per_second)%60)).zfill(2)
    min = str(int((time/ticks_per_second)/60))
    timer = gamebox.from_text(650, 100, "Time remaining " + min + ":" + sec + "." + frac, "Arial", 24, "white")
    if pygame.K_RIGHT in keys:
        character.x += 5
    if pygame.K_LEFT in keys:
        character.x -= 15
    character.yspeed += 1
    character.y = character.y + character.yspeed
    for wall in walls:
        if character.bottom_touches(wall):
            character.yspeed = 0
            if pygame.K_SPACE in keys:
                character.yspeed -= 20
        if character.touches(wall):
            character.move_to_stop_overlapping(wall)
    if character.x < 0:
        character.x = 800
    if character.x > 800:
        character.x = 0
    if character.y < 0:
        character.y = 600
    if character.y > 600:
        character.y = 0
    scorer = gamebox.from_text(150, 100, "Score: " + str(score), 'Arial', 24, 'white')
    camera.draw(timer)
    camera.draw(character)
    camera.draw(scorer)
    for coin in coins:
        coin.yspeed += .125
        coin.y = coin.y + coin.yspeed
        if character.touches(coin):
            score += 10
            coins.remove(coin)
        camera.draw(coin)
    # add more coins whenever we start to run out with len(coins) > 2
    # I'm going to add coins at a certain time (once a second)
    if time % 30 == 0:
        new_coin = gamebox.from_color(random.randint(50, 750), -10, 'yellow', 12, 12)
        coins.append(new_coin)
    # make our platforms fall
    for platform in platforms:
        platform.y += 3
        # move the platform back to the top when it goes below the screen
        if platform.top > camera.bottom:
            # if we say camera.bottom + 20 (or another number), it'll wait a little longer before resetting
            platform.y = 0
            platform.x = random.randrange(0, 800)
            platform.size = random.randrange(100, 500), 20
            # these variables are known by gamebox, you can see what gamebox knows in documentation
        # we want to character to stand on the platforms or jump from them
        if character.bottom_touches(platform):
            character.yspeed = 0
            if pygame.K_SPACE in keys:
                character.yspeed = -20
        if character.touches(platform):
            character.move_to_stop_overlapping(platform)
    for wall in walls:
        camera.draw(wall)
    for platform in platforms:
        camera.draw(platform)
    if time <= 0:
        camera.draw(gamebox.from_text(400, 300, "Game over !!!", 'Arial', 70, "white"))
        # stop the game when time runs out
        gamebox.pause()
    camera.display()
ticks_per_second = 30
gamebox.timer_loop(ticks_per_second, tick)