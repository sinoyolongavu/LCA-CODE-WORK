# Question 1: Using a for loop with a list

# TODO: Create a list of fruits
fruits = ["Apple" , "Banana" , "Grapes" , "Mango"]
# TODO: Use a for loop to print each fruit in the list
for fruits in fruits:
    print(fruits)
#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1
count = 5 
while count > 0:
    print(count)
    count -= 1
print("Happy new year!")
    


#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers
for number in range (1, 11):
    square = number **2
    print(square)

#-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module
import random
# TODO: Create a list of colors
colours = ["red" , "blue" , "greeen" , "black"]
# TODO: Use a for loop to select and print 3 random colors from the list
for x in range(3):
    print(random.choice (colours))

#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
"""

# TODO: Import the custom module and use its functions
import math_operations
# TODO: Use a while loop to create a simple calculator
while True:
    print("1, add")
    print("2, substact")
    print("3, multiply")
    print("4, divide")
    print("5, shutdown")

    option = input("choose from these operators (1 - 5)")
    if option == "5":
        print("shutdown")
        break

    num1 = float(input("insert any number"))
    num2 = float(input("insert any number"))

    if option == "1":
         result  = num1 + num2
    elif option == "2":
        result = num1 - num2
    elif option == "3":
        result = num1 * num2
    elif option == "4":
        if num2 == 0:
            print("error: Cannot divide by zero")
            continue
        result = num1 / num2
    else:
        print("invalid option. please try again.")
        continue
    print(result)



