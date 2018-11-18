"""
Memory game
"""

import random

def print_matrix(matrix_num, flipped):
    """
    Print the matrix grid
    """
    x_tile = 5
    y_tile = 4
    k = 0
    for i in range(y_tile):
        for j in range(x_tile):
            if flipped[k] == 1:
                print(matrix_num[k], end=" ")
            else:
                print("* ", end="")
            k += 1
        print(" ")

def rand():
    """
    Simple randomizer
    """
    rng = random.randint(0, 19)
    return rng

def shuffle(pre_shuffle_list):
    """
    shuffles the matrix list numbers
    """
    temp = 0
    for i in range(len(pre_shuffle_list)):
        j = rand()
        temp = pre_shuffle_list[i]
        pre_shuffle_list[i] = pre_shuffle_list[j]
        pre_shuffle_list[j] = temp

def main():
    """
    main loop
    """
    flipped = [] #* 20
    matrix_num = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]
    for i in range(0, 20):
        flipped.append(0)

    print(flipped)
    shuffle(matrix_num)
    print_matrix(matrix_num, flipped)

if __name__ == "__main__":
    main()
