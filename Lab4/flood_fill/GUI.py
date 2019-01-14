"""
Creates the GUI elements like the menu
"""
import graphics as graph

WINDOW_HEIGHT, WINDOW_WIDTH = 500, 500
BORD_SIZE = [6, 10, 15, 25]
STATE = ["highscore", "play", "quit"]
REPLAY = ["Yes", "No"]

def create_win():#7
    """
    Makes the game window
    """
    win = graph.GraphWin("Flood-fill", WINDOW_WIDTH, WINDOW_HEIGHT)
    return win

def create_menu(win, state):#8
    """
    Menu buttons
    """
    win.setCoords(0.0, 0.0, 30.0, 30.0)
    highscore_box = graph.Rectangle(graph.Point(10, 20), graph.Point(20, 23)).draw(win)
    highscore_box.setFill("black")

    highscore_text = graph.Text(graph.Point(15, 21.5), "Highscore").draw(win)
    highscore_text.setFill("white")
    highscore_text.setSize(20)

    play_box = graph.Rectangle(graph.Point(10, 15), graph.Point(20, 18)).draw(win)
    play_box.setFill("black")

    play_text = graph.Text(graph.Point(15, 16.5), "Play").draw(win)
    play_text.setFill("white")
    play_text.setSize(20)

    quit_box = graph.Rectangle(graph.Point(10, 10), graph.Point(20, 13)).draw(win)
    quit_box.setFill("black")

    quit_text = graph.Text(graph.Point(15, 11.5), "Quit").draw(win)
    quit_text.setFill("white")
    quit_text.setSize(20)

    click = win.getMouse()
    print(click)
    box_lst = [highscore_box, highscore_text, play_box, play_text, quit_box, quit_text]

    #Highscore
    if 10 <= click.x <= 20 and 20 <= click.y <= 23:
        state = STATE[0]

    #Play
    if 10 <= click.x <= 20 and 15 <= click.y <= 18:
        undraw_box(box_lst)
        state = STATE[1]
        #Hide menu
    #Quit
    if 10 <= click.x <= 20 and 10 <= click.y <= 13:
        state = STATE[2]

    undraw_box(box_lst)

    return state

def choose_size(win, size):#9
    """
    Bord size menu buttons
    """
    win.setCoords(0.0, 0.0, 30.0, 30.0)
    size_box_1 = graph.Rectangle(graph.Point(10, 20), graph.Point(20, 23)).draw(win)
    size_box_1.setFill("black")

    size_text_1 = graph.Text(graph.Point(15, 21.5), "6,6").draw(win)
    size_text_1.setFill("white")
    size_text_1.setSize(20)

    size_box_2 = graph.Rectangle(graph.Point(10, 16), graph.Point(20, 19)).draw(win)
    size_box_2.setFill("black")

    size_text_2 = graph.Text(graph.Point(15, 17.5), "10,10").draw(win)
    size_text_2.setFill("white")
    size_text_2.setSize(20)

    size_box_3 = graph.Rectangle(graph.Point(10, 12), graph.Point(20, 15)).draw(win)
    size_box_3.setFill("black")

    size_text_3 = graph.Text(graph.Point(15, 13.5), "15,15").draw(win)
    size_text_3.setFill("white")
    size_text_3.setSize(20)

    size_box_4 = graph.Rectangle(graph.Point(10, 8), graph.Point(20, 11)).draw(win)
    size_box_4.setFill("black")

    size_text_4 = graph.Text(graph.Point(15, 9.5), "25,25").draw(win)
    size_text_4.setFill("white")
    size_text_4.setSize(20)

    click = win.getMouse()
    box_lst = [size_box_1, size_text_1,
               size_box_2, size_text_2,
               size_box_3, size_text_3,
               size_box_4, size_text_4]

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

def gameover_screen(win_loose):#10
    """
    gameover screen
    """
    g_win = graph.GraphWin("Gameover", WINDOW_WIDTH, WINDOW_HEIGHT)
    g_win.setCoords(0.0, 0.0, 30.0, 30.0)

    if win_loose == 0:
        msg_banner_1 = graph.Text(graph.Point(15, 25), "You made it in or under the max move count").draw(g_win)
        msg_banner_1.setSize(15)
    elif win_loose == 1:
        msg_banner_2 = graph.Text(graph.Point(15, 25), "You failed").draw(g_win)
        msg_banner_2.setSize(25)

    g_win.getMouse()
    g_win.close()

def undraw_box(box_lst):#11
    """
    Undraws the menu boxes
    """
    for counter, i in enumerate(box_lst):
        box_lst[counter].undraw()
