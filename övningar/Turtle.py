import turtle

def square(size):
    angel = 90
    for i in range(0,4):
        turtle.setheading(angel)
        turtle.forward(size)
        angel =angel - 90
def triangel(size):
    angel = 0
    for i in range(3):
        turtle.setheading(angel)
        turtle.forward(size)
        angel += 120
def polygon(size, edges):
    angel = 90
    for i in range(edges):
        turtle.setheading(angel)
        turtle.forward(size)
        angel += 180-((edges - 2)*180) / edges

screen = turtle.Screen()
screen.setup(width = 600, height = 600)
turtle.mode("logo")
turtle.showturtle()
#turtle.setheading(90)
turtle.begin_fill()    # Fill the next shape
turtle.fillcolor('aqua')    # Color of filling
polygon(50, 20)
turtle.end_fill()

screen.exitonclick()