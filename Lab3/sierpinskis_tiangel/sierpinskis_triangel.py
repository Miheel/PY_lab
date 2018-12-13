"""
Sierpinskis Triangle 
"""
from graphics import *
import math

def sierpinski(win, size, start, color):
    """
    """
    p1 = start

    #Takes the starting points X value and adds the side length
    p2 = Point(start.getX() + size, start.getY())

    #Takes the sin() values and calculates the height 
    sin_g = math.sin(math.pi / 3)
    height = size * sin_g
    #Adds the sidelength to starting points X value
    #Adds the height of tri to starting points Y value
    p3 = Point(start.getX() + size / 2, start.getY() + height)

    triangle = Polygon(p1, p2, p3)
    triangle.setFill(color)
    
    if color == "white":
        color = "red"
        triangle.setFill(color)
    
    elif color == "red":
        color = "white"
        triangle.setFill(color)
    triangle.draw(win)
    
    start_p_tri = start

    #Sets the new startin point the rightmost triangel 
    #By adding half the side length to the X value
    point_r_tri = Point(start.getX() + (size / 2), start.getY())

    #Sets the new startin point the downmost triangel
    #By adding 1 forth the side side length to the X value 
    #and one half the height of the prior triangle to the Y value
    point_d_tri = Point(start.getX() + (size / 4), start.getY() + (height / 2)) 

    if size > 10:
        sierpinski(win, size / 2, start_p_tri, color)
        
        sierpinski(win, size / 2, point_r_tri, color)
        
        sierpinski(win, size / 2, point_d_tri, color)

    if size <= 5:
        return 0
       
def main():
    win = GraphWin("Triangel", 1600, 900)
    win.setBackground("green")
    side_len = 800
    col_tri = "red"
    
    #Calculates the triangels stating pos
    win_w = (win.getWidth() / 2) - (side_len / 2)
    win_h = (win.getHeight() / 2) - (side_len / 2)

    start_p = Point(win_w, win_h)

    sierpinski(win, side_len, start_p, col_tri)
    win.getMouse()

if __name__ == "__main__":
    main()
