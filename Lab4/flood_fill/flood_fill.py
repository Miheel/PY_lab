"""
Flood Fill game
"""
from graphics import *
import random

COLORS = ["cyan", "purple", "blue", "green", "yellow", "red"]
WINDOW_HEIGHT, WINDOW_WIDTH = 500, 500

def rand_grid(rect_lst):
    """
    load a list with random numbers
    """
    color_grid_lst = []
    for i in range(len(rect_lst)):
        color_grid_lst.append(random.randint(0,5))
    return color_grid_lst

def create_grid(grid_size):
    """
    lad a list with rectangles 
    """
    rect_lst = []

    box_h = WINDOW_HEIGHT // grid_size
    box_w = WINDOW_WIDTH // grid_size
    
    y = 0
    for rect_cols in range(0, WINDOW_HEIGHT, box_h):
        #walk through Window_WIDTH with box_w lenght
        x = 0
        if y < grid_size:
            for rect_rows in range(0, WINDOW_WIDTH, box_w):
                #rect_rows will offset the next rect in the x axis with box_w units
                #rect_cols will offset the next row in the y axis with box_h units
                box_p1 = Point(rect_rows, rect_cols)
                box_p2 = Point(rect_rows + box_w, rect_cols + box_h)
                if x < grid_size:
                    rect = Rectangle(box_p1, box_p2)
                    rect_lst.append(rect)
                    x += 1
            y += 1
    print(box_h)
    return rect_lst
    
def create_win():
    """
    makes the game window
    """
    win = GraphWin("Flood-fill", WINDOW_WIDTH, WINDOW_HEIGHT)

    return win
def find_color(lst, mouse_pos, size):
    """
    returns the color of the chosen rectangle
    """
    rect_num = find_rect(mouse_pos, size)

    return lst[0][rect_num]
    
def find_rect(mouse_pos, size):
    """
    finds and return the correct rectangel the mouse clicked on
    """
    x_axis = mouse_pos.getX() // (WINDOW_WIDTH // size)
    y_axis = mouse_pos.getY() // (WINDOW_HEIGHT // size)
    
    return int(y_axis * size + x_axis)

def draw_board(win, lst):
    """
    Draws out the grid of color filled rectangles
    """
    for i in range(len(lst[0])):
        color = COLORS[lst[0][i]]
        lst[1][i].setFill(color)
        lst[1][i].draw(win)      
        #print(lst[1][i], "\n")

def change_color(color, lst):
    """
    Changes color on element 0 in lst
    """
    lst[0][0] = color
    [lst[1][i].undraw() for i in range(len(lst[1]))]

def main():
    """
    main funk
    """
    size_of_grid = 6
    win = create_win()
    rect_lst = create_grid(size_of_grid)
    color_lst = rand_grid(rect_lst)

    rect_color_grid_lst = [color_lst, rect_lst]
    print(len(rect_color_grid_lst[0]))
    print(len(rect_color_grid_lst[0]))
    draw_board(win, rect_color_grid_lst)
    while True:
        color_num = find_color(rect_color_grid_lst, win.getMouse(), size_of_grid)
        print(color_num)
        change_color(color_num, rect_color_grid_lst)
        draw_board(win, rect_color_grid_lst)
        print(rect_color_grid_lst[0])



if __name__ == "__main__":
    main()
