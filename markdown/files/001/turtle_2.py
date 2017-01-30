import turtle


def draw_square():
    sides_draw_so_far = 0  # set lines_drawn to be 0     lines_drawn ← 0
    while sides_draw_so_far < 4:
        turtle.forward(100)
        turtle.right(90)
        sides_draw_so_far += 1
        # print(julio_the_clam_quibbler)


def draw_triangle():
    for i in range(3):
        turtle.forward(100)
        turtle.right(360 / 3)


def draw_pentagon():
    for i in range(5):
        turtle.forward(100)
        turtle.right(360 / 5)


def draw_polygon(sides, side_length=50):
    '''Draws a regular polygon
    draw_polygon(sides) draws a sides-sided polygon with edges of 50 pixels
    draw_polygon(s, p) draws an s-sided polygon with edges of p pixels
    '''
    for i in range(sides):
        turtle.forward(side_length)
        turtle.right(360 / sides)


# slow down so I can watch
turtle.speed('slow')
#
# draw_square()
#
# turtle.up()
# turtle.back(150)
# turtle.down()
#
# draw_triangle()
# draw_pentagon()

draw_polygon(3, 100)
draw_polygon(4, 50)
draw_polygon(5, 10)
draw_polygon(6, 100)
draw_polygon(7)
draw_polygon(8)
draw_polygon(9)
draw_polygon(-5)

turtle.mainloop()  # this keeps the window open
