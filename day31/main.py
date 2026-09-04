BACKGROUND_COLOR = "#B1DDC6"
from tkinter import  *
import pandas as pd
import random
#-------------correct function---------
def correct():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()

def wrong():
    next_card()
    pass

# -------------- Read data------
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data=pd.read_csv("data/french_words.csv")
#print(data["English"])
#ANGELA CODE
to_learn = data.to_dict(orient="records")
current_card={}
def next_card():
    global current_card
    if len(to_learn)==0:
        canvas.itemconfig(card_title,text="FINISHED !")
        canvas.itemconfig(word_text,text="NO WORD LEFT")
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(word_text, text=current_card["French"])
    canvas.itemconfig(card_background, image=card_front_img)
    window.after(3000, func=flip_card)
#MY CODE
# def pickrandom():
#     random_word= data["French"][random.randint(0,len(data)-1)]
#     canvas.itemconfig(word_text,text=random_word)

def flip_card():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(word_text,text=current_card["English"])
    canvas.itemconfig(card_background,image=card_back_img)
#------------- UI interface------------------
window = Tk()
window.title("Flash Card")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

#window.minsize(width=800,height=700)
#button
right_image= PhotoImage(file="images/right.png")
right_button = Button(image=right_image,highlightthickness=0,command=correct)
right_button.grid(column=1,row=1)
wrong_image= PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image,highlightthickness=0,command=wrong)
wrong_button.grid(column=0,row=1)

canvas = Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

card_background=canvas.create_image(400,263,image=card_front_img)
card_title=canvas.create_text(400,158,text="",font=("aerial",40,"italic"))
word_text=canvas.create_text(400,263,text="word",font=("Aerial",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)
next_card()
window.mainloop()
