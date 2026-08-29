import tkinter

window = tkinter.Tk()

window.title("My first GUI program")
window.minsize(width=500,height=350)

#label
my_label=tkinter.Label(text="I am a Label",font=("Aerial",24,"bold"))
#my_label.pack(side="left")
my_label.pack()
my_label["text"] = "CLICK BELOW"


def button_clicked():
    print("I got clicked")
    my_label.config(text="I got  Clicked ^_^")

button = tkinter.Button(text="Click Me",command=button_clicked)
button.pack()
window.mainloop()
