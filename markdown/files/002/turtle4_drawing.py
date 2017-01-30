import turtle
import random

yurtle = turtle.Turtle()
yurtle.speed("fastest")
colors = ["green", "red", "yellow", "cyan", "orange", "pink"]

def draw_square(my_turtle, x, y):
   my_turtle.penup()
   my_turtle.goto(x,y)
   my_turtle.pendown()
   for i in range(4):
       rand_color = random.randint(0,len(colors)-1)
       my_turtle.color(colors[rand_color])
       my_turtle.forward(100)
       my_turtle.left(90)

# Add code to draw 20 squares on the screen at random locations
for i in range(2000):
   rand_x = random.randint(-300,300)
   rand_y = random.randint(-300,300)
   draw_square(yurtle, rand_x,rand_y)

turtle.done()
