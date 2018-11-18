"""
Memory game
"""

import random

def print_matrix(matrix_num, taken):
    """
    Print the matrix grid
    """
    x_tile = 5
    y_tile = 4
    k = 0
    for i in range(y_tile):
        for j in range(x_tile):
            if taken[k] == 1:
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
    play_loop = True
    atempts = 0
    player_input = 0
    taken= [] #* 20
    matrix_num = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]
    for i in range(0, 20):
        taken.append(0)
    shuffle(matrix_num)

    print("Welcome to memory")
    print("Chose two coordinates in the matrix (x y)")
    while play_loop:

        while player_input < 2:
            x_input = int(input("input1 X:"))
            y_input = int(input("input2 Y:"))

            if player_input == 0:
                card_1 = y_input * 5 + x_input
            elif player_input == 1:
                card_2 = y_input * 5 + x_input
            player_input += 1

        print(matrix_num[card_1])
        print(matrix_num[card_2])
        print_matrix(matrix_num, taken)

        taken[card_1] = 1
        taken[card_2] = 1
        print_matrix(matrix_num, taken)
        print(taken)
        if 0 in taken:
            player_input = 0
        else:
            print("cleared board")
            play_loop = False



if __name__ == "__main__":
    main()

