"""
Flood Fill game
"""
import random
import graphics as graph
import GUI
import highscore as high

COLORS = ["cyan", "purple", "blue", "green", "yellow", "red", "BlanchedAlmond", "hot pink"]

def create_grid(grid_size, num_of_color):#1
    """
    load a one 2d list with rectangles and one 2d list with random runbers to represent colors
    """
    rect_lst = []
    color_lst = []

    box_h = GUI.WINDOW_HEIGHT // grid_size
    box_w = GUI.WINDOW_WIDTH // grid_size

    cols = 0
    for rect_cols in range(0, GUI.WINDOW_HEIGHT, box_h):
        #walk through Window_WIDTH with box_w lenght
        rows = 0
        rect_x = []
        color_lst_x = []

        if cols < grid_size:
            for rect_rows in range(0, GUI.WINDOW_WIDTH, box_w):

                #rect_rows will offset the next rect in the x axis with box_w units
                #rect_cols will offset the next row in the y axis with box_h units
                box_p1 = graph.Point(rect_rows, rect_cols)
                box_p2 = graph.Point(rect_rows + box_w, rect_cols + box_h)

                if rows < grid_size:
                    rect = graph.Rectangle(box_p1, box_p2)

                    color_lst_x.append(random.randint(0, num_of_color))
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
    x_axis = mouse_pos.getX() // (GUI.WINDOW_WIDTH // size)
    y_axis = mouse_pos.getY() // (GUI.WINDOW_HEIGHT // size)

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

    if new_color == start_color:
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

def draw_board(win, lst):#5
    """
    Draws out the grid of color filled rectangles
    """
    for y in range(len(lst[1])):
        for x in range(len(lst[1])):
            color = COLORS[lst[0][y][x]]
            lst[1][y][x].setFill(color)
            lst[1][y][x].draw(win)

def undraw_board(lst):#6
    """
    Hides the board
    """
    [lst[1][y][x].undraw()
     for y in range(len(lst[1]))
     for x in range(len(lst[1]))]

def main():
    """
    main funk
    """
    menu_loop = True
    state = 0
    win = GUI.create_win()

    while menu_loop:
        size_of_grid = 0
        int_x, int_y = 0, 0
        max_moves, moves = 0, 0
        game_loop = True

        highscore_lst = {
            "name": [],
            "points": []
            }
        high.read_file("highscore.txt", highscore_lst)
        state = GUI.create_menu(win, state)

        #Highscore
        if state == GUI.STATE[0]:
            high.highscore_GUI(highscore_lst)

        #Play
        if state == GUI.STATE[1]:
            size_of_grid = GUI.choose_size(win, size_of_grid)
            if size_of_grid == 6:
                num_of_color = 4
                max_moves = 20
            if size_of_grid == 10:
                num_of_color = 5
                max_moves = 17
            if size_of_grid == 15:
                num_of_color = 6
                max_moves = 29
            if size_of_grid == 25:
                num_of_color = 7
                max_moves = 60

            #rect_lst
            rect_color_grid_lst = create_grid(size_of_grid, num_of_color)
            win.setCoords(0, 500, 500, 0)

            name_out = high.input_GUI()
            draw_board(win, rect_color_grid_lst)

            while game_loop:
                color_num = find_color(rect_color_grid_lst, win.getMouse(), size_of_grid)
                print(color_num)

                change_color(rect_color_grid_lst, int_x, int_y,
                             rect_color_grid_lst[0][0][0], color_num)

                undraw_board(rect_color_grid_lst)

                draw_board(win, rect_color_grid_lst)

                #check if the bord is complete
                #return true if all element i lst are the same
                all_same = all(color_num == rect_color_grid_lst[0][x][y]
                               for x in range(len(rect_color_grid_lst[0]))
                               for y in range(len(rect_color_grid_lst[0])))

                if all_same:
                    if moves < max_moves:
                        high.add_highscore(name_out, moves, highscore_lst)
                        high.write_file("highscore.txt", highscore_lst)
                        GUI.gameover_screen(0)
                        game_loop = False
                    elif moves > max_moves:
                        GUI.gameover_screen(1)
                        game_loop = False
                moves += 1
            undraw_board(rect_color_grid_lst)

        #Quit
        if state == GUI.STATE[2]:
            menu_loop = False
            high.write_file("highscore.txt", highscore_lst)

    win.close()

if __name__ == "__main__":
    main()
