"""
    hangman
"""
import random
import os
#from collections import defaultdict
def rand_i():
    """ randomizer"""
    rng = random.randint(0, 20)
    return rng

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def read_file(infile, range_rng):
    """
    Reads specific line in file based on rand_i()
    """
    fin = open(infile, "r") #opens a file to read
    i = 0
    word = 0

    for line in fin: #Iterate over file
        if i < range_rng:
            word = list(line.strip()) #Read line number range_rng and convert to list
        i += 1
    fin.close()
    return word

def hidden_word(letter, word):
    """
    Prints out underscores that hides the word
    """
    k = 0
    for i in word: #Iterate over list "word"

        if letter["taken_letter"][k] == 1: #key "taken_letter" list index k
            print(word[k], end="")
        else:
            print("_ ", end="")
        k += 1

def make_guese(letter, word):
    """
    Guess a letter in the word
    """
    letter_in = input("\nType a letter to make a guese: ")
    k = 0
    for i in word:
        if letter_in in word:

            if letter_in == i:
                if letter["taken_letter"][k] == 1: #key "taken_letter" list index k
                    print("Guess alredy made: ")
                    break

                elif letter["taken_letter"][k] == 0: #if letter exist in the word update taken[k]
                    letter["taken_letter"][k] = 1
        else:
            print("letter not in word")
            if letter_in not in letter["wrong_letter"]: #check for letter exist in word 
                letter["wrong_letter"].append(letter_in) #append letter
            break

        k += 1
    return letter


def main():
    """main funktion"""
    #vars
    letter_dict = { 
        "taken_letter": [],
        "wrong_letter": []
    } #initialize dictionary with two empty lists
    taken_zero = 0
    tries = 0
    rand_int = rand_i()
    play_loop = True
    word = read_file("word_list.txt", rand_int)
    for i in word: #load list taken_letter with 0
        letter_dict["taken_letter"].append(taken_zero) 
    #

    print("Welcome to hangman")
    hidden_word(letter_dict, word)

    while play_loop is True:
        letter_dict = make_guese(letter_dict, word)
        hidden_word(letter_dict, word)
		
        print("\nLetters not in the word: ", end="")
        for i in range(len(letter_dict["wrong_letter"])):
            print(letter_dict["wrong_letter"][i], end="")

        if 0 in letter_dict["taken_letter"]:
            play_loop = True
            tries += 1

        else:
            cls()
            word_str = "".join(word)
            print("\nyou made it in ", tries, "tries")
            print("The word was:", word_str)
            input("")
            play_loop = False


if __name__ == "__main__":
    main()
