import time
import sys
def read_file(infile, line_start = "#0", line_stop = "#1"):
    fin = open(infile, "r")
    lines = ""
    line = 0
    for line in fin:

        if line.startswith(line_start):

            for line in fin:
                if line.strip() != line_stop:
                    lines += line 

                if line.startswith(line_stop):
                    break
    return lines

def print_text(line_start, line_end):
    text = read_file("text.txt", line_start, line_end)
    for char in text:
        print(char, end = "")
        sys.stdout.flush() 
        time.sleep(0.1)

def print_menu_opt():
    text = read_file("menu_opt.txt")
    print(text)

print_text("#0", "#1")
print_menu_opt()

