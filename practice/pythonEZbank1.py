#Steven
#EZBank 1
import basics

app = basics.newProgram()

user = basics.newUser()

app.balance = 1000

while app.running == True:
    user.choice = input("Do you want to [1] Deposit, [2] Withdraw, [3] Exit?")
    if user.choice == "1":
        user.deposit = input("How much do you want to deposit?")
        user.deposit = int(user.deposit)
        app.balance = app.balance + user.deposit

    elif user.choice == "2":
        user.withdraw = input("How much do you want to withdraw?")
        user.withdraw = int(user.withdraw)
        if user.withdraw > app.balance:
            user.choice = input("You dont have enough money")
        else:
            app.balance = app.balance - user.withdraw
            print(app.balance)

    elif user.choice == "3":
        app.running = False

    else:
        user.choice = input("Your choice was invalid")
        
        



