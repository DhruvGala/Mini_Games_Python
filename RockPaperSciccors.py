'''
Created on Oct 29, 2015

@author: DhruvGala

version log: <1.0> implemented basic functionality of Rock Papers Scissors game.
             <1.1> made it interactive by continuous playing and user inputs
             <1.2> Exception handling and input error handling
'''
import sys, random

from pip._vendor.distlib.compat import raw_input


#changes the number to choice for display purposes.
#@param number
def number_to_choice(number):
    if number == 0:
        choice = "rock"
    elif number == 1:
        choice = "paper"
    elif number == 2:
        choice = "scissors"
        
    return choice

#the actual logic of the game is implemented in here
#@param comp_choice
#@Param player_choice
def game_logic(comp_choice,player_choice):
    result = comp_choice - player_choice
    who_won =""
    if result == 1:
        who_won = "computer wins!"
    elif result == 2:
        who_won = "player wins!"
    elif result == 0:
        who_won = "Its a tie"
    elif result == -2:
        who_won = "computer wins!"
    elif result == -1:
        who_won = "player wins!"
        
    return who_won        

#runs the game, generates the random choice for computer
#and compares and displays the winner.
#@param player_choice
def display(player_choice):
    print()
    
    player = number_to_choice(player_choice)
    print("Player chooses {}".format(player))
    
    comp = random.randrange(0,2)
    comp_choice = number_to_choice(comp)
    print("Computer chooses {}".format(comp_choice))
    
    print(game_logic(comp, player_choice))
    print()

#interactive gaming, taking user input
def take_user_input():
    player_choice = raw_input("Choose:\n1.Rock\n2.Paper\n3.Scissors")
    try:
        player_choice = int(player_choice)
        if(player_choice > 3):
            raise ValueError
            
    except ValueError:
        print("Invalid input")
        sys.exit(0)
        
    #converting choice to 0 based    
    player_choice = player_choice - 1
    
    display(player_choice)


#main function
def main():
    
    #continuous gaming experience
    while(True):
        wanna_play = raw_input("ROCK PAPER SCISSORS!! (y/n)")
        if wanna_play == "y":
            take_user_input()
        elif wanna_play == "n":
            print("Thank you for playing!")
            break

if __name__ == '__main__':main()