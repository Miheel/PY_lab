"""
sten sax påse
"""
import random

def ai():
    """'
    Simple randomizer
    """
    rng = random.randint(1, 3)
    return rng

def main():
    """
    main funktion
    """
    moves = ["rock", "paper", "scissor"]
    player_points = 0
    pc_points = 0

    print("Welcome to the Game ROCK-PAPER-SCISSORS!\n")
    name = input("Please type your name ")
    print("Welcome ", name, " What's your choise\n")

    play = True
    while play:
        print("ROCK(1), PAPER(2), SCISSORS(3), or end game(0)")
        player_input = input("input: ")
        pc_choice = ai()

        if player_input in (1, 2, 3):
            if player_input == pc_choice:
                print("it'a draw\n")
            elif player_input == 1 and pc_choice == 3 or player_input == 2 and pc_choice == 1 or player_input == 3 and pc_choice == 2:
                print("congrats you win\n pc: ", moves[pc_choice-1], "\n", name, ":", moves[player_input-1], "\n")
                player_points += 1
            else:
                print("you loose\npc: ", moves[pc_choice-1], "\n", name, ":", moves[player_input-1], "\n")
                pc_points += 1
        elif player_input in ("q", "quit"):
            print(name, "have", player_points, "points.\n", "Pc have ", pc_points, "points")
            play = False
        else:
            print("invalid input\n")

if __name__ == "__main__":
    main()
