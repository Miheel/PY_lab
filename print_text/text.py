import time
import sys
def read_file(line_start, line_stop):
    fin = open("text.txt", "r")
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

text = read_file("#0", "#1")
#print(text)
for char in text:
    print(char, end = "")
    sys.stdout.flush() 
    time.sleep(0.1)

