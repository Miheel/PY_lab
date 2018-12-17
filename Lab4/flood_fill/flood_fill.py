"""
Flood Fill game
"""
import random
from graphics import *

COLORS = ["cyan", "purple", "blue", "green", "yellow", "red"]
WINDOW_HEIGHT, WINDOW_WIDTH = 500, 500

def rand_grid(rect_lst):
    """
    load a list with random numbers
    """
    color_lst = []
    for y in range(len(rect_lst)):
        color_lst_x = []
        for x in range(len(rect_lst)):
            color_lst_x.append(random.randint(0, 5))

        color_lst.append(color_lst_x)
    return color_lst

def create_grid(grid_size):
    """
    lad a list with rectangles
    """
    rect_lst = []

    box_h = WINDOW_HEIGHT // grid_size
    box_w = WINDOW_WIDTH // grid_size

    cols = 0
    for rect_cols in range(0, WINDOW_HEIGHT, box_h):
        #walk through Window_WIDTH with box_w lenght
        rows = 0
        rect_x = []

        if cols < grid_size:
            for rect_rows in range(0, WINDOW_WIDTH, box_w):

                #rect_rows will offset the next rect in the x axis with box_w units
                #rect_cols will offset the next row in the y axis with box_h units
                box_p1 = Point(rect_rows, rect_cols)
                box_p2 = Point(rect_rows + box_w, rect_cols + box_h)

                if rows < grid_size:
                    rect = Rectangle(box_p1, box_p2)

                    rect_x.append(rect)
                    rows += 1

            rect_lst.append(rect_x)
            cols += 1

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
    lst_xy = find_rect(mouse_pos, size)

    return lst[0][lst_xy[1]][lst_xy[0]]

def find_rect(mouse_pos, size):
    """
    finds and return the correct rectangel the mouse clicked on
    """
    x_axis = mouse_pos.getX() // (WINDOW_WIDTH // size)
    y_axis = mouse_pos.getY() // (WINDOW_HEIGHT // size)

    lst = [int(x_axis), int(y_axis)]
    print("point", lst)
    return lst

def draw_board(win, lst):
    """
    Draws out the grid of color filled rectangles
    """
    for y in range(len(lst[1])):
        for x in range(len(lst[1])):
            color = COLORS[lst[0][y][x]]
            lst[1][y][x].setFill(color)
            lst[1][y][x].draw(win)
            #print(lst[1][i], "\n")

def change_color(lst, start_x, start_y, start_color, new_color):
    """
    Changes color of element in lst
    """
    node_color = lst[0][start_x][start_y]
    #if node is out of range return
    if 0 > start_x > len(lst[0]) or 0 > start_y > len(lst[0]):
        return 0
    #if current node color is not equal to start color return
    if node_color != start_color:
        return 0
    
    lst[0][start_x][start_y] = new_color
	
    #if x less than the width of lst go forward one step
    if start_x < len(lst[0][start_x])-1:
        #East
        change_color(lst, start_x + 1, start_y, start_color, new_color)

    #if x bigger than 0 go back one step
    if start_x > 0:
        #West
        change_color(lst, start_x - 1, start_y, start_color, new_color)

    #if y less than height of lst go up one step
    if start_y < len(lst[0][start_y]) - 1:
        #South
        change_color(lst, start_x, start_y + 1, start_color, new_color)
    
    #if y bigger than 0 go up one step
    if start_y > 0:
        #North
        change_color(lst, start_x, start_y - 1, start_color, new_color)




def main():
    """
    main funk
    """
    size_of_grid = 10
    int_x, int_y = 0, 0
    win = create_win()
    rect_lst = create_grid(size_of_grid)
    color_lst = rand_grid(rect_lst)

    rect_color_grid_lst = [color_lst, rect_lst]
    print(rect_color_grid_lst[0])

    draw_board(win, rect_color_grid_lst)
    while True:
        color_num = find_color(rect_color_grid_lst, win.getMouse(), size_of_grid)
        print(color_num)

        change_color(rect_color_grid_lst, int_x, int_y, color_lst[0][0], color_num)

        [rect_color_grid_lst[1][y][x].undraw() for y in range(len(rect_color_grid_lst[1])) for x in range(len(rect_color_grid_lst[1]))]
        draw_board(win, rect_color_grid_lst)
        #print(rect_color_grid_lst)

if __name__ == "__main__":
    main()
