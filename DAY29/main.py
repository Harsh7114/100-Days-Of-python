from tkinter import *
import random
from  tkinter import  messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))] #new_item for item in list
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    #to save on clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0:
        messagebox.showinfo(
            title="OOPS",
            message="Please enter website"
        )

    elif len(password) < 5:
        messagebox.showinfo(
            title="OOPS",
            message="Enter password greater than 5 digit"
        )

    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered:\nEmail: {email}"
                    f"\nPassword: {password}\nIs it ok to save?"
        )

        if is_ok:
            try:
                # READ existing data
                with open("password.json", "r") as f:
                    data = json.load(f)

                # ADD new data
                data.update(new_data)

                # WRITE updated data
                with open("password.json", "w") as f:
                    json.dump(data, f, indent=4)
            except (FileNotFoundError,json.JSONDecodeError):
                with open("password.json", "w") as f:
                    json.dump(new_data, f, indent=4)

            website_entry.delete(0, END)
            password_entry.delete(0, END)
    #window.destroy()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
#label
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)
password_label = Label(text="Password:")
password_label.grid(row=3,column=0)
#entries
website_entry = Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(END,"harshranjan2582779@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)
#button
generate_Pass = Button(text="Generate Password",command=generate_password)
generate_Pass.grid(column=2,row=3)
add_button = Button(text="ADD",width=36,command=save_pass)
add_button.grid(row=4,column=1,columnspan=2)
canvas= Canvas(width=200,height=200,bg='white',highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=image)
canvas.grid(column=1,row=0)

window.mainloop()