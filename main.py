from tkinter import *
from random import *
import pandas as pd
# import time
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- FLASH CARDS ------------------------------- #
df = pd.read_csv("data/Korea.csv")
df.to_dict(orient="records")

def guess():
    global translation
    rand = choice(df.values)
    word = rand[0]
    translation = rand[1]
    canvas.itemconfig(canvas_image, image=front_img)
    canvas.delete("txt")
    canvas.create_text(400, 263, text=f"{word}", font=("Ariel", 60, "bold"), tags="txt")
    window.after(3000, swap_bg)

def swap_bg():

    canvas.itemconfig(canvas_image, image=back_img)
    canvas.delete("txt")
    canvas.create_text(400, 263, text=f"{translation}", font=("Ariel", 60, "bold"), tags="txt")
    # window.after_cancel(swap)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Flash Card")
window.config(pady=50, padx=50, background=BACKGROUND_COLOR)

front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")

# ---------- BUTTONS ---------- #

right = PhotoImage(file="images/right.png")
right_button = Button(image=right, highlightthickness=0, command=guess)
right_button.grid(column=1, row=2)

wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, command=guess)
wrong_button.grid(column=0, row=2)


canvas = Canvas(width=800, height=526)
canvas_image = canvas.create_image(400, 263, image=front_img)
canvas.configure(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_text(400, 150, text="Korean", font=("Ariel", 40, "italic"))
canvas.create_text(400, 315, text="For latin speakers", font=("Ariel", 13, "bold"))
canvas.grid(column=0, row=0, columnspan=2, rowspan=2)


mainloop()
