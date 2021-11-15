# Steven Miller
# practice using expressions and conditonal statments

# an expression is a problem that must be solved
# 5 + 5 is an "arithmetic" expression
x = 5 + 5

# Functions/methods must be resolved as expression as well
answer = input("What is your name?")

# Comparison expression resolve as True/False
print( 7 > 7 )
print( 7 >= 7 )
print( x == 10 )
print( x > 10 or x < 10 )

#A conditional statment runs if its condition is True / not False
if answer == "Bob":
    print("Hello, Bob! Welcome back!")
    print("This line also print if your name is Bob")
elif answer == "Vadim":
    print("Hay you still owe me money!")
else:
    print("Sorry, I only talk to Bobs")
print("This line isn't inside of the if statment, and prints regard:")

# ^ If checks a condition
# ^ Elif checks a condition if the previous conditions were not True
# ^ You can have as many elif's as you want
# ^ Elis run if no prior conditions were true
    
age = input("how old are you?")
age = int(age)
if age >= 10:
    print("Here is your license")
elif age >= 9:
    print("Come back when your 1 older.") 
else:
    print("Your to young.")
     
