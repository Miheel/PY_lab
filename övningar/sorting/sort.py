import random

def rand():
    rng = random.randint(0,100)
    return rng

def sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

def insert(seq):
    for i in range(1, len(seq)):
        temp = seq[i]
        temp_pos = i

        while temp_pos > 0 and seq[temp_pos-1] > temp:
            seq[temp_pos] = seq[temp_pos - 1]
            temp_pos -= 1

        seq[temp_pos] = temp


def read(infile):
    fin = open(infile, "r")
    temp = []
    for i in fin:
        temp.append(int(i))
    return temp

def write_f(outfile, arr):
    fout = open(outfile, "w")
    for i in arr:
        fout.write(str(i) + "\n")

file_1 = read("arr.txt")
file_2 = read("arr.txt")
sort(file_1)
insert(file_2)
write_f("new_arr_bub.txt", file_1)
write_f("new_arr_ins.txt", file_2)

print("sorted")
for i in range(len(file_1)):
    print(str(file_1[i]) + " ", end="")
print("\n")
for i in range(len(file_2)):
    print(str(file_2[i]) + " ", end="")
