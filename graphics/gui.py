from graphics import *

window = GraphWin("window", 300, 300)
center = Point(50, 50)
circle = Circle(center, 10)
circle.setFill("Green")
circle.draw(window)
while  True:
    if window.getKey() == "Up":
        circle.move(0, -1)
    if window.getKey() == "Down":
        circle.move(0, 1)
    if window.getKey() == "Left":
        circle.move(-1, 0)
    if window.getKey() == "Right":
        circle.move(1, 0)

input("")
