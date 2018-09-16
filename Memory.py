# implementation of card game - Memory
# http://www.codeskulptor.org/#user45_Psl9E4vTswF1ALq.py

import simplegui
import random

deck = range(8) + range (8)
turns = 0

# helper function to initialize globals
def new_game():
    global exposed, state, click1, click2, turns
    random.shuffle(deck)
    exposed = [False]*16
    click1 = click2 = state = turns = 0
    label.set_text("Turns = " + str(turns))

# define event handlers
def mouseclick(pos):
    global state, click1, click2, turns
    i = pos[0] // 50
    if exposed[i] == False:
        exposed[i] = True
        if state == 0:
            state = 1
            click1 = i
        elif state == 1:
            state = 2
            click2 = i
            turns += 1
        else:
            if deck[click1] != deck[click2]:
                exposed[click1] = exposed[click2] = False
            state = 1
            click1 = i
        label.set_text("Turns = " + str(turns))
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    k = 0
    for i in range(16):
        if exposed[i] == True:
            canvas.draw_text(str(deck[i]), [10 + k, 70], 60, 'White')
        else:
            canvas.draw_polygon([(k, 0), (k, 100), (50 + k, 100), (50 + k, 0)], 
                                2, 'Red', 'Green')
        k += 50


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " + str(turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
