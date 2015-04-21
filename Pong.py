# Implementation of classic arcade game Pong

import simplegui
import random

#parameters
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [2,-2]
ball_vel_start = [2,-2]
paddle1_pos = HEIGHT/2
paddle2_pos = HEIGHT/2
paddle1_vel = 0
paddle2_vel = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left

def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    x = random.random()
    if x>0.5:
        y = 1
    else:
        y = -1;
    if direction == RIGHT:
        ball_vel = [-2,y*2]
    elif direction == LEFT:
        ball_vel = [2,y*2]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  
    # these are numbers
    global score1, score2 
    score1 = 0
    score2 = 0
   
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "Green")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "Blue")
        
    # update ball
    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    global paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos 
    if paddle2_pos <= PAD_HEIGHT/2 and paddle2_vel < 0:
        paddle2_pos = paddle2_pos
    elif paddle2_pos >= HEIGHT-PAD_HEIGHT/2 and paddle2_vel > 0:
        paddle2_pos = paddle2_pos
    else:
        paddle2_pos = paddle2_pos + paddle2_vel
    
    if paddle1_pos <= PAD_HEIGHT/2 and paddle1_vel < 0:
        paddle1_pos = paddle1_pos
    elif paddle1_pos >= HEIGHT-PAD_HEIGHT/2 and paddle1_vel > 0:
        paddle1_pos = paddle1_pos
    else:
        paddle1_pos = paddle1_pos + paddle1_vel
        
    canvas.draw_line((PAD_WIDTH/2, paddle1_pos-PAD_HEIGHT/2), (PAD_WIDTH/2, paddle1_pos+PAD_HEIGHT/2), PAD_WIDTH, 'White')
    canvas.draw_line((WIDTH-PAD_WIDTH/2, paddle2_pos-PAD_HEIGHT/2), (WIDTH-PAD_WIDTH/2, paddle2_pos+PAD_HEIGHT/2), PAD_WIDTH, 'White')
    
    # determine whether paddle and ball collide
    
    if ball_pos[1] >= (HEIGHT-BALL_RADIUS) or ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - (ball_vel[1])
        
    if ball_pos[0] >= (WIDTH - BALL_RADIUS-PAD_WIDTH):
        if (abs(ball_pos[1]-paddle2_pos) < PAD_HEIGHT/2+BALL_RADIUS):
            ball_vel[0] = - (ball_vel[0] + 0.1*ball_vel[0])
        else:
            score1 = score1+1
            spawn_ball(LEFT)
      
    if (ball_pos[0] <= BALL_RADIUS+PAD_WIDTH):
        if (abs(ball_pos[1]-paddle1_pos) < PAD_HEIGHT/2+BALL_RADIUS):
            ball_vel[0] = - (ball_vel[0] + 0.1*ball_vel[0])
        else:
            score2 = score2 +1
            spawn_ball(RIGHT)
    
    # draw scores
    canvas.draw_text(str(score1), (WIDTH/4, 20), 22, 'Green')
    canvas.draw_text(str(score2), [3*WIDTH/4, 20], 22, 'Blue')
        
def keydown(key):
    global paddle1_vel, paddle2_vel, paddle2_pos
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = 10
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = -10
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 10
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel = -10
    
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0

def reset_handler():
    global score1, score2
    score1 = 0
    score2 = 0
    x = random.random()
    if x>0.5:
        spawn_ball(RIGHT)
    else:
        spawn_ball(LEFT)
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Reset', reset_handler, 50)

# start frame
new_game()
frame.start()
