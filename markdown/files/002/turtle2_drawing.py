# This example uses prewritten libraries (or modules) called turtle and random.
# A library is a collection of code, written and compiled by someone else,
# that is ready for you to use in your program

import turtle
import random

# def defines a function
# A function is reusable piece of code
def draw_square(t, x, y):

    t.penup()         # Pull the pen up – no drawing when moving
    t.goto(x,y)       # positions to start point x,y
    t.pendown()       # Pull the pen down – drawing when moving

    # chooses a random color from color list below
    rand_color = random.randint(0,len(colors)-1)

    t.color(colors[rand_color])   # set pencolor and fillcolor

    # draw four sides
    for i in range(4):
        t.forward(100)    # Move the turtle forward by the specified distance
        t.left(90)        # Turn turtle left by 90 degree

tom = turtle.Turtle()     # Create a turtle named tom
tom.speed("fast")         # Set tom's speed

# Create a list of color for later randomly used when drawing
colors = ["green", "red", "yellow", "orange", "pink", "cyan"]

# Call a function draw_square
draw_square(tom, 100, 100)

# Draw 10 times
# for i in range(10):
#     rand_x = random.randint(-100,100)
#     rand_y = random.randint(-100,100)
#     draw_square(tom, rand_x, rand_y)


turtle.done()