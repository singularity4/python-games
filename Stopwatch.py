# template for "Stopwatch: The Game"
import simplegui

# define global variables
global time, x, y, boolean
time = 0
x = 0
y = 0
boolean = 0

def format(t):
    h = t /(60*60*10)
    t = t % (60*60*10)
    m = (t / (60*10))%60
    t = t % (60*10)
    sec = (t / 10)%60
    t = t % 10
    ds = t
    
    if sec < 10:
        sec_str = '0' + str(sec)
    else: sec_str = str(sec)
    
    x = str(m) + ':' + str(sec_str) + '.' + str(ds)
    return x
    
# define event handlers for buttons; "Start", "Stop", "Reset"

def start_handler():
    timer.start()
    global boolean
    boolean = 1

    
def stop_handler():
    timer.stop()
    global y, boolean
    y = y + 1
    if (format(time)[5] == '0') and (boolean == 1):
        global x
        x = x + 1
    boolean = 0
        
    
def reset_handler():
    timer.stop()
    global time, boolean
    time = 0
    boolean = 1
    timer.start()
    
    

# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time = time + 1

# define draw handler

def draw_handler(frame):
    frame.draw_text(format(time), (100, 100), 24, 'White')
    frame.draw_text(str(x) + '/' + str(y), (232, 10), 12, 'Grey')

    
# create frame
frame = simplegui.create_frame("Stopwatch", 250, 200)


# register event handlers

frame.set_draw_handler(draw_handler)
frame.add_button('Start', start_handler, 50)
frame.add_button('Stop', stop_handler, 50)
frame.add_button('Reset', reset_handler, 50)
timer = simplegui.create_timer(100, tick)


# start frame
frame.start()

    
