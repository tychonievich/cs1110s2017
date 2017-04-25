wish = '''
using mouse
sound
flip sprites
resize player

grid-based motion
end game on objective
options menu
play again
computer vs human
'''


import pygame
import gamebox
camera = gamebox.Camera(800,600)
logo = gamebox.from_image(0, 0, "spritesheet.png")

music = gamebox.load_sound("http://www.gnu.org/fun/jokes/eternal-flame.ogg")

music.play()

# make a method that will be called every frame. Must have parameter “keys”
def tick(keys):
    camera.clear('white')
    if pygame.K_UP in keys:
        # you can check which keys are being pressed
        print("the up arrow key is currently being pressed")
    if camera.mouseclick:
    # true if some mouse button is being pressed
        logo.center = camera.mouse
    # the current mouse position
    camera.draw(logo)
    camera.display()

# tell gamebox to call the tick method 30 times per second
gamebox.timer_loop(30, tick)
# this line of code will not be reached until after the window is closed