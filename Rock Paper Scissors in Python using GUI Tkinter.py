import random as rand
from tkinter import *
from tkinter import messagebox

def reset():  # This will randomly select the move
    global p1_choice, p2_choice
    b1['text'] = 'Player 1 Roll'
    b1['state'] = NORMAL
    p1.configure(image = general['player_1'])
    p1_choice = None
    b2['text'] = 'Player 2 Roll'
    b2['state'] = NORMAL
    p2.configure(image = general['player_2'])
    p2_choice = None

