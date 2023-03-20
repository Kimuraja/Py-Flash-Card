from tkinter import *
from random import *
import pandas as pd
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- FLASH CARDS ------------------------------- #
df = pd.read_csv("data/Korea.csv")
my_list = [i for i in df.to_dict(orient="records")]
random_choice = choice(my_list)


def good_answer():
    global random_choice
    random_choice = choice(my_list)
    new_df = pd.DataFrame(my_list)
    canvas.itemconfig(canvas_image, image=front_img)
    canvas.delete("txt")
    canvas.delete("enter")
    canvas.delete("eng")
    canvas.create_text(400, 150, text="Korean", font=("Ariel", 50, "italic"), tags="black_title", fill="black")
    canvas.create_text(400, 263, text=f"{random_choice['Korean']}", font=("Ariel", 70, "bold"), tags="txt",
                       fill="black")
    canvas.create_text(400, 330, text="For latin speakers", font=("Ariel", 15, "bold"), tags="latin", fill="black")
    window.after(3000, swap_bg)
    my_list.remove(random_choice)
    new_df.to_csv('./data/words_to_learn.csv')


def wrong_answer():
    canvas.itemconfig(canvas_image, image=front_img)
    canvas.delete("txt")
    canvas.delete("enter")
    canvas.delete("eng")
    canvas.create_text(400, 150, text="Korean", font=("Ariel", 50, "italic"), tags="black_title", fill="black")
    canvas.create_text(400, 263, text=f"{random_choice['Korean']}", font=("Ariel", 70, "bold"), tags="txt",
                       fill="black")
    canvas.create_text(400, 330, text="For latin speakers", font=("Ariel", 15, "bold"), tags="latin", fill="black")
    window.after(3000, swap_bg)


def swap_bg():
    canvas.delete("black_title")
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.delete("txt")
    canvas.delete("latin")
    canvas.create_text(400, 150, text="English", font=("Ariel", 50, "italic"), tags="eng", fill="white")
    canvas.create_text(400, 263, text=f"{random_choice['English']}", font=("Ariel", 60, "bold"), tags="txt",
                       fill="white")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Flash Card")
window.config(pady=50, padx=50, background=BACKGROUND_COLOR)

front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")


# ---------- BUTTONS ---------- #

right = PhotoImage(file="images/right.png")
right_button = Button(image=right, highlightthickness=0, command=good_answer)
right_button.grid(column=1, row=2)

wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, command=wrong_answer)
wrong_button.grid(column=0, row=2)


canvas = Canvas(width=800, height=526)
canvas_image = canvas.create_image(400, 263, image=front_img)
canvas.configure(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_text(400, 230, text="Click any button to start", font=("Ariel", 40, "bold"), tags="enter", fill="black")
canvas.grid(column=0, row=0, columnspan=2, rowspan=2)


mainloop()