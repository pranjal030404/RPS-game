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

def compare():   # This will compare the moves of both players
    if ((b1['text'][0] == 'R' and b2['text'][0] == 'S') or (b1['text'][0] == 'S' and b2['text'][0] == 'P') or (b1['text'][0] == 'P' and b2['text'][0] == 'R')):
        messagebox.showinfo('Victory', 'Player 1 has Won.')
    elif b1['text'] == b2['text']:
        messagebox.showinfo('Draw', "It's a tie.")
    else:
        messagebox.showinfo('Victory', 'Player 2 has Won.')
    reset()

def check():  # This will check if both states are DISABLED or not
    if b1['state'] == b2['state'] == DISABLED:
        compare()

def player1_roll():  # Player1 will randomly select the move
    global p1_choice
    p1_choice = rand.choice(['rock', 'scissors', 'paper'])
    p1.configure(image = moves[p1_choice])
    b1['text'] = p1_choice.title()
    b1['state'] = DISABLED
    check()

def player2_roll():  # Player2 will randomly select the move
    global p2_choice
    p2_choice = rand.choice(['rock', 'scissors', 'paper'])
    p2.configure(image = moves[p2_choice])
    b2['text'] = p2_choice.title()
    b2['state'] = DISABLED
    check()

# Main Program
root = Tk()
root.title("Rock-Paper-Scissors")
font = (('Arial','bold'),'20')
general = {'player_1': PhotoImage(file = 'logo/player1.png'), 'player_2': PhotoImage(file = 'logo/player2.png'), 'vs': PhotoImage(file = 'logo/vs.png')}
moves = {'rock': PhotoImage(file = 'logo/rock.png'), 'paper': PhotoImage(file = 'logo/paper.png'), 'scissors': PhotoImage(file = 'logo/scissor.png')}
f1 = Frame(root)
p1 = Label(f1, image = general['player_1'])
p1.pack(side = 'left')
vs = Label(f1, image = general['vs'])
vs.pack(side = 'left')
p2 = Label(f1, image = general['player_2'])
p2.pack(side = 'left')
f1.pack()
f2 = Frame(root)
b1 = Button(f2, text = 'Player 1 Roll', width = 20, font = font, command = player1_roll)
b1.pack(side = 'left')
f_space = Frame(f2, width = 150)
f_space.pack(side = 'left')
b2 = Button(f2, text = 'Player 2 Roll', width = 20, font = font, command = player2_roll)
b2.pack(side = 'left')
f2.pack(pady = 10)
p1_choice = None
p2_choice = None
root.mainloop()