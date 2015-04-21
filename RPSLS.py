# Rock-paper-scissors-lizard-Spock 
# Open in CodeSkulptor: http://www.codeskulptor.org/#user39_3bS9J6TdFu_1.py

import random

def name_to_number(name):
    # converts name to a number 
    if name == "rock":
        name = 0
    elif name == "Spock":
          name = 1
    elif name == "paper":
          name = 2
    elif name == "lizard":
          name = 3
    elif name == "scissors":
          name = 4
    else: 
        print "Please enter a valid option"
    return name

def number_to_name(number):
    # converts number to a name
    if number == 0:
        number = "rock"
    elif number == 1:
          number = "Spock"
    elif number == 2:
          number = "paper"
    elif number == 3:
          number = "lizard"
    elif number == 4:
          number = "scissors"
    else: 
        print "Please enter a valid number"
    return number
    
def rpsls(player_choice):  
    print ""
    print "Player chooses", player_choice
    
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses", comp_choice

    difference = (comp_number - player_number) % 5

    if difference == 1 or difference == 2:
        print "Computer wins!"
    elif difference == 3 or difference == 4:
        print "Player wins!"
    elif difference == 0:
        print "Computer and player tie"
    return difference

   
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

