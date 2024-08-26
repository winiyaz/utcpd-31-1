# Solution for the project

from tkinter import *

# --------------------- Constants --------------------- #
BOOTY_COLOR = "#400036"
CF_IMG = "img/cf.png"
CB_IMG = "img/cb.png"
WRONG = "img/wrong.png"
RIGHT = "img/right.png"
TXT_FG = "#F2059F"
TXT_BFG = "#22BABB"

# --------------------- Window Setup --------------------- #
window = Tk()
window.title("AssAndPussy")
window.config(padx=50, pady=50, bg=BOOTY_COLOR)

# --------------------- CanvasObjet --------------------- #

canvas = Canvas(width=800, height=526, highlightthickness=0)
cf_img = PhotoImage(file=CF_IMG)
canvas.create_image(400, 263, image=cf_img)
canvas.create_text(400,150, text="Title", font=("Helvetica", 40, "italic"), fill=TXT_FG)
canvas.create_text(400,263, text="word", font=("Verdana", 60, "bold"), fill=TXT_BFG)

canvas.config(bg=BOOTY_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

# --------------------- UI --------------------- #

wr_img = PhotoImage(file=WRONG)
no_but = Button(image=wr_img, highlightthickness=0, bg=BOOTY_COLOR)
no_but.grid(row=1, column=0)

r_img = PhotoImage(file=RIGHT)
yes_but = Button(image=r_img, highlightthickness=0, bg=BOOTY_COLOR)
yes_but.grid(row=1, column=1)


# --------------------- Window Start Loop --------------------- #
window.mainloop()
