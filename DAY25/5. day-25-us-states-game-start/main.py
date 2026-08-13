import turtle

screen= turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"
#load a new image as shape
screen.addshape(image)
turtle.shape(image)
#WE CAN USE THIS FUNCTION TO MAP THE COORDINATE ON SCREEN BUT IN OUR PROJEXT WE ARE GOINT TO TAKE FROM CSV FILE

# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)

answer = screen.textinput(title="Guess the state",prompt="What is the name of state")
print(answer)
#mainloop used to keep screen open just like exit on click
turtle.mainloop()
# screen.exitonclick()