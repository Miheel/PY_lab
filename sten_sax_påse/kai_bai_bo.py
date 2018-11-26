"""
 kai bai bo
"""
import random

def rand():
    """'
    Simple randomizer
    """
    rng = random.randint(1, 3)
    return rng

def main():
    """
    main funktion
    """
    moves = ["Rock", "Paper", "Scissor"]
    player_points = 0
    pc_points = 0
    play_loop = True

    print("Welcome to the Game ROCK-PAPER-SCISSORS!\n")
    name = input("Please type your name ")
    print("Welcome ", name, " What's your choise\n")

    while play_loop:
        print("ROCK(1), PAPER(2), SCISSORS(3), or end game(q or quit)")
        player_input = input("input: ") #input to str

        pc_choice = str(rand()) #convert value from rand int to str

        if player_input in ("1", "2", "3"):

            if player_input == pc_choice: #Argument for a draw
                print("it'a draw\npc: ", moves[int(pc_choice)-1])
                print(name, ":", moves[int(player_input)-1], "\n")
            
            #Argument for a player wim
            elif player_input == "1" and pc_choice == "3" or player_input == "2" and pc_choice == "1" or player_input == "3" and pc_choice == "2":
                
                #takes value from list moves to write out move instead number
                print("congrats you win\npc: ", moves[int(pc_choice)-1])
                print(name, ":", moves[int(player_input)-1], "\n")
                player_points += 1

            else: #Argument for a player win
                print("you loose\npc: ", moves[int(pc_choice)-1])
                print(name, ":", moves[int(player_input)-1], "\n")
                pc_points += 1

        elif player_input in ("q", "quit"): #Argument to end th game
            print(name, "have", player_points, "points.\nPc have ", pc_points, "points.")
            print("Exiting game")
            input("Press enter exit")
            play_loop = False

        else:
            print("invalid input\n")

if __name__ == "__main__":
    main()
