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
    return arr
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

file_ = read("arr.txt")
sort(file_)
write_f("new_arr.txt", file_)

print("sorted")
for i in range(len(file_)):
    print(file_[i])



#test arr
arr1 = []
for i in range(0,50):
    rng = rand()
    arr1.append(rng)

print("arr1")
for i in range(len(arr1)):
    print(arr1[i])
write_f("arr1.txt", arr1)

sort(arr1)

print("arr sorted")
print("\n")
for i in range(len(arr1)):
    print(arr1[i])

write_f("arr2.txt", arr1)
