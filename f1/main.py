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
ACTIVE_B_FG_W = "#FF204E"
ACTIVE_B_FG_R = "#06D001"
DATA_FILE = "dt/f_w.csv"

# --------------------- Function  --------------------- #

da = pa.read_csv(DATA_FILE)
to_learn = da.to_dict(orient="records")



def next_card():
	cu_card = ra.choice(to_learn)
	canvas.itemconfig(card_title, text="French")
	canvas.itemconfig(card_word, text=cu_card["French"])



# --------------------- Window Setup --------------------- #
window = Tk()
window.title("AssAndPussy")
window.config(padx=100, pady=100, bg=BOOTY_COLOR)

# --------------------- CanvasObjet --------------------- #

canvas = Canvas(width=800, height=526, highlightthickness=0)
cf_img = PhotoImage(file=CF_IMG)
canvas.create_image(400, 263, image=cf_img)
card_title = canvas.create_text(400, 150, font=("Helvetica", 40, "italic"), fill=TXT_FG)
card_word = canvas.create_text(400, 263, font=("Verdana", 50, "bold"), fill=TXT_BFG)

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
				 command=next_card)
yes_but.grid(row=1, column=1)

# --------------------- Window Start Loop --------------------- #
window.mainloop()
