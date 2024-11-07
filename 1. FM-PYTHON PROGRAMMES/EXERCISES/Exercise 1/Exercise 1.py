# Question 1: Variable Assignment and String Manipulation

# TODO: Ask the user for their name and store it in a variable
name = input("What is your name: ")
# TODO: Ask the user for their age and store it in a variable
age = input("How old are you: ")
# TODO: Print a greeting using the name and age variable 
print(f"Hello,{name}! you old {age} years old.")

#------------------------------------------------------------------------------------
# Question 2: Integer Operations

# TODO: Ask the user for the length of a rectangle and store it as an integer
length = int(input("length of the rectangle: "))
# TODO: Ask the user for the width of a rectangle and store it as an integer
width = int(input("width of rectangle: "))
# TODO: Calculate the area of the rectangle
area = length * width
# TODO: Print the result
print(f"area of rectangle: {area} ")
#------------------------------------------------------------------------------------
# Question 3: Working with Floats

# TODO: Ask the user for a temperature in Celsius and store it as a float
Celsius = float(input(("what is the temperature in celsius:")))
# TODO: Convert the temperature to Fahrenheit using the formula: (C * 9/5) + 32
Fahrenheit = (Celsius * 9/5) + 32
# TODO: Print the result rounded to two decimal places
print(f"the temperature in Fahrenheit is: {Fahrenheit:.2f}")