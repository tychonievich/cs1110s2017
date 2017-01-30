import turtle

def drawShape(t, sides, size):
    angle = 360.0 / sides

    for i in range(sides):
        if t.color()[0] == "red":
            t.color("black")
        else:
            t.color("red")

        t.forward(size)
        t.left(angle)

dana = turtle.Turtle()
drawShape(dana, 6, 100)
dana.right(180)
drawShape(dana, 5, 100)

turtle.done()