# import the basics module to use its code
import basics

# make a new application object from the basics module
app = basics.newProgram()

# use a method that belongs to our new application object
app.print("yo momma")

# print a property of our new application object
app.print( app.debugging )

# this line wont print if app.debugging is false
app.debug('Hello')

# we'll enable debugging for application
app.debugging = True
app.debug('Now it works!')

# import a default Python module
import random

# use the method from the random module
randomNumber = random.randint(1, 10)
app.print(randomNumber)
