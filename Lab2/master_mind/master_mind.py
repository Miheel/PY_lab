"""
Master mind game
"""

import random
from master_mind_GUI import *

def rand_list():
    """
    randomizing a combination of colors
    """
    guess_list = []
    for i in range(4):
        guess_list.append(random.randint(0, 5))
    return guess_list

def correct(pc_combi, guess_combi):
    """
    calculate how many colors are in the correct place
    """
    corr_place = 0
    for i in range(4):
        if pc_combi[i] == guess_combi[i]:
            corr_place += 1
    return corr_place

def corr_wrong(pc_combi, guess_combi):
    """
    calculates how many colors are correct
    """
    corr_wrong_place = 0
    for i in range(4):
        if guess_combi[i] in pc_combi:
            corr_wrong_place += 1
    return corr_wrong_place

def main():
    """
    main
    """
    guess = 0
    winn_loose = ["Looser", "Winner"]
    pc_rand_list = rand_list()
    print(pc_rand_list)
    game_win = create_GUI()
    play_loop = True

    while play_loop is True:
        corr_place_int = 0
        wrong_plce_int = 0

        make_guess_list = make_guess(guess, game_win)
        
        corr_place_int = correct(pc_rand_list, make_guess_list)
        
        corr_wrong_place_int = corr_wrong(pc_rand_list, make_guess_list)
        
        wrong_place_int = corr_wrong_place_int - corr_place_int

        peg_feedback(guess, corr_place_int, wrong_place_int, game_win)

        if corr_place_int == 4:
            gameover_screen(guess, winn_loose[1])
            play_loop = False
        elif guess == 6:
            gameover_screen(guess, winn_loose[0])
            play_loop = False

        guess += 1
        print(guess)


if __name__ == "__main__":
    main()
