"""
    hangman
"""
import random
def rand_i():
    """ randomizer"""
    rng = random.randint(0, 20)
    return rng

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
    return word

def hidden_word(taken_letter, word):
    """
    Prints out underscores that hides the word
    """
    k = 0
    for i in word: #Iterate over list "word"

        if taken_letter[k] == 1:
            print(word[k], end="")
        else:
            print("_ ", end="")
        k += 1

def make_guese(taken, word):
    """
    Guess a letter in the word
    """
    letter = input("\nmake a guese: ")
    k = 0
    for i in word:
        if letter in word:

            if letter == i:
                if taken[k] == 1:
                    print("Guess alredy made: ")
                    break

                elif taken[k] == 0: #if letter exist in the word update taken[k]
                    taken[k] = 1
        else:
            print("letter not in word")
            break

        k += 1
    return taken

def main():
    """main funktion"""
    #vars
    taken_letter = []
    taken_zero = 0
    tries = 0
    rand_int = rand_i()
    play_loop = True
    word = read_file("word_list.txt", rand_int)
    for i in word:
        taken_letter.append(taken_zero)
    #

    print("Welcome to hangman")
    hidden_word(taken_letter, word)

    while play_loop is True:
        #print(taken)
        #print(word)
        taken_letter = make_guese(taken_letter, word)
        hidden_word(taken_letter, word)
        if 0 in taken_letter:
            play_loop = True
            tries += 1

        else:
            word_str = "".join(word)
            print("\nyou made it in ", tries, "tries")
            print("The word was: ", word_str)
            play_loop = False


if __name__ == "__main__":
    main()
