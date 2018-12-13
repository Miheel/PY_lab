"""
Flood Fill game
"""
from graphics import *
import random

COLORS = ["cyan", "purple", "blue", "green", "yellow", "red"]

def rand_grid(rect_lst):
    """
    load a list with random numbers
    """
    color_grid_lst = []
    for i in range(len(rect_lst)):
        color_grid_lst.append(random.randint(0,5))
    return color_grid_lst


def create_grid(win):
    """
    lad a list with rectangles 
    """
    rect_lst = []
    win_h = win.getHeight() / 5
    win_w = win.getWidth() / 5
    start_p1 = Point(0.0, 0.0)
    start_p2 = Point(start_p1.getX() + win_w , start_p1.getY() + win_h)
    
    rect_cols = 0
    p1_Y = 0
    p2_Y = win_h
    
    while rect_cols < 500:
        p1_X = 0
        p2_X = win_w
        rect_rows = 0
    
        if rect_cols == 0:
            p2_Y = start_p2.getY()
        else:
            p1_Y += start_p1.getY() + start_p2.getY()
            p2_Y += start_p1.getY() + start_p2.getY()
        i = 0
        while rect_rows < 500:
            #adds the length of the rect to startpoint1s x value
            #to offset the next rect
            p1_X += start_p2.getX() * i
            p1_XY = Point(p1_X, p1_Y)
            
            #adds the length of the rect to startpoint2s y value
            #to offset the next rect
            p2_X += start_p2.getX() * i
            p2_XY = Point(p2_X, p2_Y)
 
            i = 1
 
            rect = Rectangle(p1_XY, p2_XY)
            rect_lst.append(rect) 
            rect_rows += win_w
        rect_cols += win_h
    return rect_lst
    

def create_win():
    """
    makes the game window
    """
    win = GraphWin("Flood-fill", 500, 500)

    return win

def main():
    """
    main funk
    """
    win = create_win()
    rect_lst = create_grid(win)
    color_lst = rand_grid(rect_lst)

    rect_color_grid_lst = [color_lst, rect_lst]

    for i in range(len(rect_lst)):
        rect_color_grid_lst[1][i].draw(win)
        color = COLORS[rect_color_grid_lst[0][i]]
        rect_color_grid_lst[1][i].setFill(color)
    
    print(rect_color_grid_lst)

    win.getMouse()


if __name__ == "__main__":
    main()
