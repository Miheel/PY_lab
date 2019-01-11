from graphics import *

POINTS = [64, 32, 16, 8, 4, 2, 1]

def read_file(infile, high_dict_list):
    """
    Read file and load names and points in to dict
    """
    try:    
        fin = open(infile, "r")
    except FileNotFoundError:
        fin = open(infile, "w+")

    for lines in fin:
        split(lines, high_dict_list)
    return high_dict_list

def write_file(outfile, high_dict_list):
    """
    Writes the content of dict to file 
    """
    
    fout = open(outfile, "w")
    
    for i in range(len(high_dict_list["points"])):
        fout.write(high_dict_list["name"][i] + " ")
        fout.write(high_dict_list["points"][i] + "\n")

def split(string, high_dict_list):
    """
    Splits each line in to "name" and "points"
    """
    
    for char_i in range(len(string)):
        if string[char_i] == " ":
            high_dict_list["name"].append(string[0:char_i])
            high_dict_list["points"].append(string[char_i + 1:].strip("\n"))
    return high_dict_list

def sort_high_list(high_dict_list):
    """
    Sorts lists in dict 
    """
    
    name = high_dict_list["name"]
    points = high_dict_list["points"]

    for i in range(len(points)):

        for j in range(len(points)):

            if int(points[i]) > int(points[j]):
                temp_points = points[i]
                points[i] = points[j]
                points[j] = temp_points

                temp_name = name[i]
                name[i] = name[j]
                name[j] = temp_name

    return high_dict_list

def add_highscore(name_in, guesses, high_dict_list):
    """
    Adds highscore listing to highscore list
    """

    name_list = high_dict_list["name"]
    points_list = high_dict_list["points"]
    
    
    if name_in in name_list:
        for i in range(len(name_list)):
            if name_in == name_list[i]:
                points_list[i] = int(points_list[i])
                points_list[i] += POINTS[guesses]
                points_list[i] = str(points_list[i])
            
    else:
        name_list.append(name_in)
        points_list.append(str(POINTS[guesses]))

def input_GUI():
    """
    creats the name input window
    """
    loop_ = True

    win = GraphWin("input", 500, 300)         
    win.setCoords(0, 0, 10, 10)

    in_banner_msg = Text(Point(5, 7), "Type your name followed by clicking the window").draw(win)
    in_banner_msg.setSize(15)

    while loop_ is True:
        name_in = Entry(Point(5, 5), 7).draw(win)    
        win.getMouse()

        if name_in.getText():
            loop_ = False

        else:
            empty_msg = Text(Point(5, 4), "Type youre name").draw(win)
            empty_msg.setSize(20)
            loop_ = True
    win.close()

    return name_in.getText()

def highscore_GUI(high_dict_list):
    """
    Draws the highscore list on screen
    """

    sort_high_list(high_dict_list)

    text_pos_y= 8
    h_win = GraphWin("Highscore", 500, 500)
    h_win.setCoords(0.0, 0.0, 10.0, 10.0)
    h_win.setBackground("Black")

    name = high_dict_list["name"]
    points = high_dict_list["points"]

    banner_msg = Text(Point(5, 9), "Highscore!").draw(h_win)
    banner_msg.setTextColor("White")
    banner_msg.setSize(20)
    
    if name:
        for i in range(0, len(name)):
            h_name_msg = Text(Point(4.5, text_pos_y), name[i] + ":").draw(h_win)
            h_points_msg = Text(Point(6, text_pos_y), points[i]).draw(h_win)

            h_name_msg.setTextColor("White")
            h_name_msg.setSize(20)

            h_points_msg.setTextColor("White")
            h_points_msg.setSize(20)

            text_pos_y -= 1

    h_win.getMouse()