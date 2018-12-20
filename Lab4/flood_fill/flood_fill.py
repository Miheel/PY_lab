"""
Flood Fill game
"""
import random
from graphics import *
from highscore import *

COLORS = ["cyan", "purple", "blue", "green", "yellow", "red"]
WINDOW_HEIGHT, WINDOW_WIDTH = 600, 700
BOARD_SIZE = 500
GRID = [[6,6],[10,10],[15,15],[25,25]]
GAME_STATE = ["Highscore", "Play", "Quit"]
GAMEOVER = ["Winner", "Looser"]

def create_grid(grid_size):#1
    """
    load a one 2d list with rectangles and one 2d list with random runbers to represent colors
    """
    rect_lst = []
    color_lst = []
	
    box_h = BOARD_SIZE // grid_size
    box_w = BOARD_SIZE // grid_size

    cols = 0
    for rect_cols in range(0, BOARD_SIZE, box_h):
        #walk through Window_WIDTH with box_w lenght
        rows = 0
        rect_x = []
        color_lst_x = []
		
        if cols < grid_size:
            for rect_rows in range(0, BOARD_SIZE, box_w):

                #rect_rows will offset the next rect in the x axis with box_w units
                #rect_cols will offset the next row in the y axis with box_h units
                box_p1 = Point(rect_rows, rect_cols)
                box_p2 = Point(rect_rows + box_w, rect_cols + box_h)

                if rows < grid_size:
                    rect = Rectangle(box_p1, box_p2)
					
                    color_lst_x.append(random.randint(0, 5))
                    rect_x.append(rect)
                    rows += 1
					
            color_lst.append(color_lst_x)	
            rect_lst.append(rect_x)
            cols += 1
    seq = [color_lst, rect_lst]
    return seq

def find_color(lst, mouse_pos, size):#2
    """
    returns the color of the chosen rectangle
    """
    lst_xy = find_rect(mouse_pos, size)

    return lst[0][lst_xy[1]][lst_xy[0]]

def find_rect(mouse_pos, size):#3
    """
    finds and return the correct rectangel the mouse clicked on
    """
    x_axis = mouse_pos.getX() // (BOARD_SIZE // size)
    y_axis = mouse_pos.getY() // (BOARD_SIZE // size)

    lst = [int(x_axis), int(y_axis)]
    print("point", lst)
    return lst

def change_color(lst, start_x, start_y, start_color, new_color):#4
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

def create_win():#5
    """
    makes the game window
    """
    win = GraphWin("Flood-fill", WINDOW_WIDTH, WINDOW_HEIGHT)

    return win

def create_menu(win, state):#6
    #win = GraphWin("Flood_fill", WINDOW_WIDTH, WINDOW_HEIGHT)
    win.setCoords(0.0, 0.0, 30.0, 30.0)
    
    highscore_box = Rectangle(Point(10, 20), Point(20, 23)).draw(win)
    highscore_box.setFill("black")

    highscore_text = Text(Point(15, 21.5), "Highscore").draw(win)
    highscore_text.setFill("white")
    highscore_text.setSize(20)

    play_box = Rectangle(Point(10, 15), Point(20, 18)).draw(win)
    play_box.setFill("black")

    play_text = Text(Point(15, 16.5), "Play").draw(win)
    play_text.setFill("white")
    play_text.setSize(20)
    
    quit_box = Rectangle(Point(10, 10), Point(20, 13)).draw(win)
    quit_box.setFill("black")

    quit_text = Text(Point(15, 11.5), "Quit").draw(win)
    quit_text.setFill("white")
    quit_text.setSize(20)

    click = win.getMouse()
    print(click)
    box_lst = [highscore_box, highscore_text, play_box, play_text, quit_box, quit_text]

    #Highscore
    if 10 <= click.x <= 20 and 20 <= click.y <= 23:
        state = 0

    #Play
    if 10 <= click.x <= 20 and 15 <= click.y <= 18:
        state = 1
        #Hide menu
    #Quit
    if 10 <= click.x <= 20 and 10 <= click.y <= 13:
        state = 2
    
    for i in range(len(box_lst)):
        box_lst[i].undraw()

    return state

def draw_board(win, lst):#7
    """
    Draws out the grid of color filled rectangles
    """
    for y in range(len(lst[1])):
        for x in range(len(lst[1])):
            color = COLORS[lst[0][y][x]]
            lst[1][y][x].setFill(color)
            lst[1][y][x].draw(win)

def main():
    """
    main funk
    """
    #input
    size_of_grid = 4

    int_x, int_y = 0, 0
    state = 0
    game_loop = True
    
    highscore_lst = {
            "name": [],
            "points": []
            }
    read_file("highscore.txt", highscore_lst)

    win = create_win()
    #rect_lst 
    rect_color_grid_lst = create_grid(size_of_grid)
    #color_lst = rand_grid(rect_lst)
    #rect_color_grid_lst = [color_lst, rect_lst]
    
    print(rect_color_grid_lst[0])
    print(rect_color_grid_lst[1])
    while game_loop == True:
        state = create_menu(win, state)
        win.setCoords(0,500,500,0)
        
        #Highscore
        if state == 0:
            highscore_GUI(highscore_lst)

        #Play
        if state == 1:
            name_out = input_GUI()
            draw_board(win, rect_color_grid_lst)
            while True:
                click = win.getMouse()
                if click.x < 100 or click.y < 50:
                    click.x += 100
                    click.y += 50
                if click.x > 600 or click.y > 550:
                    click.x -= 100
                    click.y -= 50

                color_num = find_color(rect_color_grid_lst, click, size_of_grid)
                print(color_num)

                change_color(rect_color_grid_lst, int_x, int_y, rect_color_grid_lst[0][0][0], color_num)

                [rect_color_grid_lst[1][y][x].undraw() for y in range(len(rect_color_grid_lst[1])) for x in range(len(rect_color_grid_lst[1]))]
                draw_board(win, rect_color_grid_lst)

                #if bord complete with moves<max_moves
                    #add_highscore()
                    #gameover_screen Winner
                #else
                    #gameover_screen looser

        #Quit
        if state == 2:
            game_loop = False
            write_file("highscore.txt", highscore_lst)
            
    win.close()

if __name__ == "__main__":
    main()
