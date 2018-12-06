"""
Test file
"""
from highscore import *
def main():
    """
    main
    """
    highscore_list = {
        "name": [],
        "points": []
    }

    read_file("highscore.txt", highscore_list)

    write_file("highscore_sort.txt", highscore_list)

    print(highscore_list["name"])
    for i in range(len(highscore_list["points"])):
        print(highscore_list["points"][i].strip())

    highscore_GUI(highscore_list)

if __name__ == "__main__":
    main()
