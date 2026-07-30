# Create a no geussing game from 1 to 100 with easy and hard mode
import  random
num=random.randint(1,100)
#print(num)
print("Welcome to no guessing Game !")
print("I am thinking of a number between 1 to 100")
def difficulity(resp):
    if resp == "easy":
        return 10
    elif resp =="hard":
        return 5
    else:
        return 0
resp =input("Choose a difficulity level Type 'easy' or 'hard'")
total_chance = difficulity(resp)
#print(total_chance)

#using loop logic
"""
for i in range(total_chance):
    if total_chance == 0:
        print("You Lost")
    print(f"You have {i} chance left to guess the correct no ")
    guessed_no = int(input("make a guess:"))
    if guessed_no == num:
        print ("you won ^_^")
    elif guessed_no > num:
        print("too High guess")
        total_chance = total_chance - 1
    elif guessed_no < num:
        print("too low guess")
        total_chance = total_chance - 1
    else:
        print("you lost")"""



#using recursion
def guess(total_chance):
    if total_chance == 0:
        return "You Lost"
    print(f"You have {total_chance} chance left to guess the correct no ")
    guessed_no = int(input("make a guess:"))

    if guessed_no == num:
        return "you won ^_^"
    elif guessed_no>num:
        print("too High guess")
        total_chance=total_chance-1
        return guess(total_chance)
    elif guessed_no<num:
        print("too low guess")
        total_chance=total_chance-1
        return guess(total_chance)
    else:
        return "you lost"

print(guess(total_chance))





