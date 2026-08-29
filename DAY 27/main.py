import tkinter
def button_clicked():
    #print("I got clicked")
    text = input.get()
    my_label.config(text=text)
window = tkinter.Tk()

window.title("My first GUI program")
window.minsize(width=500,height=350)

#label
my_label = tkinter.Label(text="I am a Label",font=("Aerial",24,"bold"))
#my_label.pack(side="left")
my_label.place(x=0,y=0)
my_label.grid(column=0,row=0)
my_label.pack()
my_label["text"] = "CLICK BELOW"


#Entry
input = tkinter.Entry(width=10)
print(input.get())
input.pack()


button = tkinter.Button(text="Click Me",command=button_clicked)
button.pack()




window.mainloop()
