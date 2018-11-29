"""
    hangman
"""
import random
def rand_i():
    """ randomizer"""
    rng = random.randint(0, 20)
    return rng

def read_file(infile, range_r):
    """Read file"""
    fin = open(infile, "r")
    i = 0
    word = 0
    for line in fin:
        if i < range_r:
            word = list(line.strip())
        i += 1
    return word

def hidden_word(word, taken):
    k = 0
    for i in word:
        if taken[k] == 1:
            print(word[k], end = "")
        else:
            print("*", end = "")
        k += 1

def make_guese(taken, word):
    letter = input("make a guese: ")
    k = 0
    for i in word:
        if letter == i:
            if taken[k] == 1:
                print("Guess alredy made: ")
                break
            elif taken[k] == 0:
                taken[k] = 1
        k += 1
    return taken


def main():
    """main funktion"""
    #vars
    taken = []
    n = 0
    tries = 0
    rng = rand_i()
    play_loop =True
    word = read_file("word_list.txt", rng)
    for i in word:
        taken.append(n)
    #

    while play_loop == True:
        #print(taken)  
        #print(word)
        make_guese(taken, word)
        hidden_word(word, taken)
        if 0 in taken:
            play_loop = True
            tries += 1
        else:
            print("you made it in ", tries, "tries")
            play_loop = False


if __name__ == "__main__":
    main()
