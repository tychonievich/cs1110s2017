import turtle
import random

def draw_polygon(sides, side_length=50):
    '''Draws a regular polygon
    draw_polygon(sides) draws a sides-sided polygon with edges of 50 pixels
    draw_polygon(s, p) draws an s-sided polygon with edges of p pixels
    '''
    for i in range(sides):
        turtle.forward(side_length)
        turtle.right(360 / sides)


turtle.speed('fastest')
# draw_polygon(5)
# turtle.shape('turtle')
# turtle.turtlesize(3, 5)
#
# turtle.circle(150, 360, 4)

def draw_star(side_length):
    for step in range(5):
        turtle.forward(side_length)
        turtle.right(144)


# draw_star(50)
# turtle.right(36)
# turtle.penup()
# turtle.forward(100)
# turtle.pendown()
# turtle.left(36)
# draw_star(50)


# sides = input('How many sides? ')
# number = int(sides)
# draw_polygon(number)

# turtle.pencolor('red')
# turtle.width(10)
#
# while True:
#     turtle.width(random.randint(1,10))
#     sides = random.randint(3,20)
#     draw_polygon(sides)

angle = ((5**0.5 - 1) / 2) * 360
distance = 0

while True:
    turtle.penup()
    turtle.forward(5*distance**0.5)
    turtle.pendown()
    turtle.dot()
    turtle.penup()
    turtle.backward(5*distance**0.5)
    turtle.left(angle)
    distance += 1







turtle.mainloop()  # this keeps the window open
