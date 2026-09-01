from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)
#label
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)
website_text=Text()
email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)
password_label = Label(text="Password:")
password_label.grid(row=3,column=0)
#entries
website_entry = Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)


canvas= Canvas(width=200,height=200,bg='white',highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=image)
canvas.grid(column=1,row=0)

window.mainloop()