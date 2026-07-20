from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}



try:
    data = pandas.read_csv("data/words_to_learn.csv.csv")
except FileNotFoundError:

   

    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



def next_card():
    
    ''' Show next random card in French '''


    global current_card
    global flip_timer
    window.after_cancel(flip_timer)   
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_front, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)   # Flip after 3 seconds



def flip_card():

    '''Remove word from learning list when user knows it '''
    
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_front, image=card_back_image)



def is_correct():

    ''' Save remaining words '''
    
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv")   
    next_card()



window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)



canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")

card_front = canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))



wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_correct)
right_button.grid(row=1, column=1)

next_card()   # Show first card

window.mainloop()
