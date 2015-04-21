#Memory game
#Open in CodeSkulptor: http://www.codeskulptor.org/#user39_EFyQQWQFkY_3.py

import simplegui
import random

height = 100
width = 800
card_width = 50
card_height = 100
card1 = 0
card2 = 0
turns = 0

def new_game():
    global deck1, deck2, card_deck, exposed, state, turns
    
    state = 0 #start of the game
    turns = 0
    label.set_text("Turns = "+str(turns))
    
    #generates card deck
    deck1 = range(1,9)
    deck2 = range(1,9)
    card_deck = deck1 + deck2
    random.shuffle(card_deck)
    
    #generates exposed card deck
    exposed = []
    for card in range(0, len(card_deck)):
        exposed.append(False)
        
def mouseclick(pos):
    global exposed, state, index, card1, card2, turns
    
    
    if pos[0] <= 800:
        index = (pos[0] / card_width)
        
    if (exposed[index] == True):
        return
    
    exposed[index] = True
    
    #main game logic goes here
    if state == 0:
        state = 1
        card1 = index
    elif state == 1:
        state = 2
        card2 = index
        turns = turns + 1
    else:
        state = 1
        if card_deck[card1] != card_deck[card2]:
            exposed[card1] = False
            exposed[card2] = False
        card1 = index
     
    
    label.set_text("Turns = "+str(turns))
    return
                   
def draw(canvas):
    global deck1, deck2, card_deck, exposed
    
    #draw cards
    delta = 0
    for card in range(0, len(card_deck)): 
        if exposed[card] == True:
            canvas.draw_text(str(card_deck[card]), (card_width/2 + delta*card_width, height/2), 22, 'White')
            canvas.draw_line((card_width + delta*card_width, 0), (card_width + delta*card_width, card_height), 2, 'White')
            delta = delta +1
        else:
            canvas.draw_line((card_width/2 + delta*card_width, 0), (card_width/2 + delta*card_width, card_height), card_width, 'Red')
            canvas.draw_line((card_width + delta*card_width, 0), (card_width + delta*card_width, card_height), 2, 'Black')
            delta = delta + 1
            
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
