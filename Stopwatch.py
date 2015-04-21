import simplegui
import random
import math

# first game

global num_range, guess_range
guess_range = 7
num_range = 100

# generic game

def new_game():
    global secret_number, guess_limit
    secret_number = random.randrange(0,num_range)
    guess_limit = guess_range
    
def range100():
    global num_range, guess_range
    num_range = 100
    guess_range = 7
    new_game()

def range1000():
    global num_range, guess_range
    num_range = 1000
    guess_range = 10
    new_game()
    
def input_guess(guess):
    guess = int(guess)
    print "Guess was", guess
    global guess_limit
    if (guess_limit > 0):
        print "The number of remaining guesses is", guess_limit
        if guess < secret_number:
            print "Higher!" 
        elif guess > secret_number:
            print "Lower!" 
        elif guess == secret_number:
            print "Correct!"  
        guess_limit = guess_limit - 1
    elif guess_limit == 0:
        print "Game over"   
    return guess

f = simplegui.create_frame("Guess the number", 200, 200)
f.add_input("Enter a guess", input_guess, 200)
f.add_button("Range is (0,100)", range100, 200)
f.add_button("Range is (0,1000)", range1000, 200)

#calls first game

new_game()
