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
    player_input = 0
    tries = 0
    taken = [] #* 20
    matrix_num = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]
    for i in range(0, 20):
        taken.append(0) #Loads th lost with 0

    shuffle(matrix_num)

    print("Welcome to memory")
    print("Chose two coordinates in the matrix (x y)")
    print_matrix(matrix_num, taken)

    while play_loop:

        while player_input < 2: #Input loop 

            x_input = int(input("input1 X:"))
            y_input = int(input("input2 Y:"))

            if 0 <= x_input < 5 and 0 <= y_input < 4: #Check if input is inside list interval
                if player_input == 0:
                    card_1 = y_input * 5 + x_input

                elif player_input == 1:
                    card_2 = y_input * 5 + x_input
                tries += 1
                player_input += 1
            else:
                print("invalid input")

        print(matrix_num[card_1])
        print(matrix_num[card_2])

        if matrix_num[card_1] == matrix_num[card_2]: #Determines if the cards are equal
            taken[card_1] = 1
            taken[card_2] = 1
            print_matrix(matrix_num, taken)
        else:
            print("the cards were not equal try again")

        print(taken)

        if 0 in taken: #Determines if the board has bee filed
            player_input = 0
        else:
            print("cleared board")
            print("It took you: ", tries)
            play_loop = False

if __name__ == "__main__":
    main()
