# this code is from the examples page
import pygame
import gamebox
camera = gamebox.Camera(800, 600)
# we need a collection of images to simulate movement
# people make these and publish them free online, they are called "sprites"
# look at the link to see the individual frames in the "spritesheet"
# gamebox.load_sprite_sheet interprets file link, rows, images per row (columns)
sheet = gamebox.load_sprite_sheet("https://estelle.github.io/10/files/sprite.png", 1, 22)
frame = 0
direction = 0
counter = 0
# this tells us which frame to start with
character = gamebox.from_image(200, 200, sheet[frame])
def tick(keys):
    global frame
    global direction
    # if we started in the middle, we could go either direction
    global counter
    frame += 1
    counter += 1
    # because we go back to 0 at 10, we are only seeing the first 10 images
    # it looks different with all 22
    if frame == 10:
        frame = 0
    # determines how often it moves; this is every 2 ticks, % 3 would be every 3 ticks, etc--% 30 is every second
    if counter % 2 == 0:
        character.image = sheet[frame+direction*10]
    camera.clear("cyan")
    camera.draw(character)
    camera.display()
ticks_per_second = 30
gamebox.timer_loop(ticks_per_second, tick)