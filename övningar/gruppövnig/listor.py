a_list = [13, 34, 55, 3, 8, 1, 21, 2, 89, 5, 1]

def list_min_for(list_in, num):
    new_list = []
    for i in list_in:
        if i < num:
            new_list.append(i)
    return new_list

def list_min_while(list_in, num):
    new_list = []
    i = 0
    while i < len(list_in):
        if list_in[i] < num:
            new_list.append(list_in[i])
        i += 1
    return new_list

def write_to_file(list_in):
    fin = open ("list.txt", "w")
    for i in range(len(list_in)):
        num = str(list_in[i])
        fin.write(num + "\n")

def main():
    num = input("A number")


if __name__ == "__main__":
    main()



# print(list_min_for(a_list, 40))
# print(list_min_while(a_list, 40))