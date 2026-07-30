# cofee machine
import sys

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },

    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },

    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 400,
    "milk": 200,
    "coffee": 100,
}

profit=0

#print report func
def print_report():
    print(f"Water:{resources['water']}")
    print(f"Milk:{resources['milk']}")
    print(f"Coffee:{resources['coffee']}")
    print("Money:",profit)


#resourse check
def is_sufficient_res(choice):
    requirement=MENU[choice]["ingredients"]
    for item in requirement:
        if requirement[item]>resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

#inserted coin
def process_coin():
    quat = int(input("insert Quarters :"))
    dimes = int(input("insert Dimes :"))
    nickle = int(input("insert Nickles :"))
    penny = int(input("insert Pennies :"))
    total_amt = (0.25*quat)+(0.10*dimes)+(0.05*nickle)+(0.01*penny)
    return total_amt
#inside a loop or function
while True:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()

    #turn off machine
    if choice=="off":
        sys.exit()
    elif choice == "report":
        print_report()
    else:
        if is_sufficient_res(choice):
            print("Insert Coin")
            amt = process_coin()
            if amt < MENU[choice]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            elif amt == MENU[choice]["cost"]:
                profit=profit+MENU[choice]["cost"]
                #decrease resourse items value by brewed cofee
                ingredents = MENU[choice]["ingredients"]
                for item in ingredents:
                    resources[item]- ingredents[item]
                print(f"Here is your {choice}. Enjoy")
                #print_report()
            else:
                change = round(amt-MENU[choice]["cost"],2)
                print(f" Here is your {change}$ in change")
                profit = profit + MENU[choice]["cost"]
                ingredents = MENU[choice]["ingredients"]
                for item in ingredents:
                    resources[item] -= ingredents[item]
                print(f"Here is your {choice}. Enjoy")
