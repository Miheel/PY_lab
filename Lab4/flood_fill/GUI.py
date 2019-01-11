from graphics import *

WINDOW_HEIGHT, WINDOW_WIDTH = 500, 500
BORD_SIZE = [6, 10, 15, 25]

def create_win():#6
    """
    makes the game window
    """
    win = GraphWin("Flood-fill", WINDOW_WIDTH, WINDOW_HEIGHT)

    return win

def create_menu(win, state):#7
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
        undraw_box(box_lst)
        state = 1
        #Hide menu
    #Quit
    if 10 <= click.x <= 20 and 10 <= click.y <= 13:
        state = 2
    
    return state

def choose_size(win, size):#8
    win.setCoords(0.0, 0.0, 30.0, 30.0)
    size_box_1 = Rectangle(Point(10, 20), Point(20, 23)).draw(win)
    size_box_1.setFill("black")

    size_text_1 = Text(Point(15, 21.5), "6,6").draw(win)
    size_text_1.setFill("white")
    size_text_1.setSize(20)

    size_box_2 = Rectangle(Point(10, 16), Point(20, 19)).draw(win)
    size_box_2.setFill("black")

    size_text_2 = Text(Point(15, 17.5), "10,10").draw(win)
    size_text_2.setFill("white")
    size_text_2.setSize(20)
    
    size_box_3 = Rectangle(Point(10, 12), Point(20, 15)).draw(win)
    size_box_3.setFill("black")

    size_text_3 = Text(Point(15, 13.5), "15,15").draw(win)
    size_text_3.setFill("white")
    size_text_3.setSize(20)
	
    size_box_4 = Rectangle(Point(10, 8), Point(20, 11)).draw(win)
    size_box_4.setFill("black")

    size_text_4 = Text(Point(15, 9.5), "25,25").draw(win)
    size_text_4.setFill("white")
    size_text_4.setSize(20)
	
    click = win.getMouse()
    box_lst = [size_box_1, size_text_1, size_box_2, size_text_2, size_box_3, size_text_3, size_box_4, size_text_4]
	
    if 10 <= click.x <= 20 and 20 <= click.y <= 23:
        size = BORD_SIZE[0]

    if 10 <= click.x <= 20 and 16 <= click.y <= 19:
        size = BORD_SIZE[1]

    if 10 <= click.x <= 20 and 12 <= click.y <= 15:
        size = BORD_SIZE[2]
		
    if 10 <= click.x <= 20 and 8 <= click.y <= 11:
        size = BORD_SIZE[3]
    
    undraw_box(box_lst)
	
    return size
	
def undraw_box(box_lst):#9
    for i in range(len(box_lst)):
        box_lst[i].undraw()