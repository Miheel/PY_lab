"""
Master mind game
"""

import random
from master_mind_GUI import *
from highscore import *

def rand_list():
    """
    randomizing a combination of colors
    """
    guess_list = []
    for i in range(4):
        guess_list.append(random.randint(0, 5))
    return guess_list

def correct_place(pc_combi, guess_combi):
    """
    calculate how many colors are in the correct place
    """
    corr_place = 0
    for i in range(4):
        if pc_combi[i] == guess_combi[i]:
            corr_place += 1
    return corr_place

def col_wrong_place(pc_combi, guess_combi):
    """
    calculates how many colors are correct
    """
    corr_wrong_place = 0
    for i in range(4):
        if pc_combi[i] in guess_combi:
            corr_wrong_place += 1
    return corr_wrong_place

def main():
    """
    main
    """
    guess = 0
    winn_loose = ["Looser", "Winner"]
    pc_rand_list = rand_list()
    game_wind = create_GUI()
    play_loop = True
    
    #NEW# 
    highscore_list = {
            "name": [],
            "points": []
            }
    
    read_file("highscore.txt", highscore_list)

    name_out = input_GUI()
    ####

    while play_loop is True:
        corr_place_num = 0
        wrong_place_num = 0

        player_guess_list = make_guess(guess, game_wind)
        
        corr_place_num = correct_place(pc_rand_list, player_guess_list)
        
        wrong_place_num = col_wrong_place(pc_rand_list, player_guess_list)
        
        wrong_place_num = wrong_place_num - corr_place_num

        peg_feedback(guess, corr_place_num, wrong_place_num, game_wind)

        if corr_place_num == 4:
            gameover_screen(guess + 1, winn_loose[1])
            
            #NEW#
            add_highscore(name_out, guess, highscore_list)
            ####
			
            play_loop = False
        
        elif guess == 6:
            gameover_screen(guess, winn_loose[0])
            play_loop = False

        guess += 1
        print(guess)
    
    #NEW#
    highscore_GUI(highscore_list)

    write_file("highscore.txt", highscore_list)
    ####

if __name__ == "__main__":
    main()
