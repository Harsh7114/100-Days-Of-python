from tkinter import *
window = Tk()
window.title("Miles to KM conveter")
window.minsize(width=100,height=100)
window.config(padx=20,pady=20)
def miles_to_Km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f"{km}")

#widget 1
miles_input = Entry()
miles_input.config(width=5)
miles_input.grid(column =1 ,row=0)
#widget 2
miles_label = Label(text="Miles")
miles_label.grid(column = 2,row=0)

is_equal_label = Label(text="is equal to ")
is_equal_label.grid(column= 0,row= 1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1,row=1)

kilometer_label = Label(text="KM")
kilometer_label.grid(column=2,row = 1)

calculate_button = Button(text="Calculate",command=miles_to_Km)
calculate_button.grid(column=1,row=2)


window.mainloop()