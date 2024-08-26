# Solution for the project

import random as ra
from tkinter import *

import pandas as pa

# --------------------- Constants --------------------- #
BOOTY_COLOR = "#400036"
CF_IMG = "img/cf.png"
CB_IMG = "img/cb.png"
WRONG = "img/wrong.png"
RIGHT = "img/right.png"
TXT_FG = "#F2059F"
TXT_BFG = "#22BABB"
N_TXT_FG = "#06D001"
N_TXT_BFG = "#FFC700"
ACTIVE_B_FG_W = "#FF204E"
ACTIVE_B_FG_R = "#06D001"
DATA_FILE = "dt/f_w.csv"
TO_LEARN_CSV = "dt/to_learn.csv"

# --------------------- Function  --------------------- #

to_learn = {}
cu_card = {}

try:
	da = pa.read_csv(TO_LEARN_CSV)
except FileNotFoundError:
	da = pa.read_csv(DATA_FILE)
	to_learn = da.to_dict(orient="records")
else:
	to_learn = da.to_dict(orient="records")


def next_card():
	global cu_card, flip_timer
	window.after_cancel(flip_timer)
	cu_card = ra.choice(to_learn)
	canvas.itemconfig(card_title, text="French", fill=TXT_FG)
	canvas.itemconfig(card_word, text=cu_card["French"], fill=TXT_BFG)
	canvas.itemconfig(card_bg, image=cf_img)
	flip_timer = window.after(3000, func=flip_card)


def flip_card():
	canvas.itemconfig(card_title, text="Englez", fill=N_TXT_FG)
	canvas.itemconfig(card_word, text=cu_card["English"], fill=N_TXT_BFG)
	canvas.itemconfig(card_bg, image=cb_img)


def is_known():
	to_learn.remove(cu_card)
	da2 = pa.DataFrame(to_learn)
	da2.to_csv("dt/to_learn.csv", index=False)
	next_card()


# --------------------- Window Setup --------------------- #
window = Tk()
window.title("AssAndPussy")
window.config(padx=100, pady=100, bg=BOOTY_COLOR)

flip_timer = window.after(3000, func=flip_card)

# --------------------- CanvasObjet --------------------- #

canvas = Canvas(width=800, height=526, highlightthickness=0)
cf_img = PhotoImage(file=CF_IMG)
cb_img = PhotoImage(file=CB_IMG)
card_bg = canvas.create_image(400, 263, image=cf_img)
card_title = canvas.create_text(400, 150, font=("Helvetica", 40, "italic"), fill=TXT_FG)
card_word = canvas.create_text(400, 263, font=("Verdana", 50, "bold"), fill=TXT_BFG)

# Intialize the card
next_card()

canvas.config(bg=BOOTY_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

# --------------------- UI --------------------- #

wr_img = PhotoImage(file=WRONG)
no_but = Button(image=wr_img, highlightthickness=0, bg=BOOTY_COLOR, activebackground=ACTIVE_B_FG_W, relief="flat",
				command=next_card)
no_but.grid(row=1, column=0)

r_img = PhotoImage(file=RIGHT)
yes_but = Button(image=r_img, highlightthickness=0, bg=BOOTY_COLOR, activebackground=ACTIVE_B_FG_R, relief="flat",
				 command=is_known)
yes_but.grid(row=1, column=1)

# --------------------- Window Start Loop --------------------- #
window.mainloop()
