# Question 1: Creating and Modifying Lists

# TODO: Create a list of fruits
fruit = ["apple" , "banana" , "grapes" , "mango"]
# TODO: Add a fruit to the end of the list
fruit.append("orange")
# TODO: Insert a fruit at the beginning of the list
fruit.insert(0, "lemon" )
# TODO: Remove a fruit from the list
fruit.pop(3)
# TODO: Print the modified list
print(fruit)
#-------------------------------------------------------------------------
# Question 2: List Operations

# TODO: Create a list of numbers from 1 to 5
numbers = list(range(1-6))
# TODO: Create a new list with each number squared
numbers = [1 , 2 , 3, 4 , 5]
squared_numbers = [x**2 for x in numbers]
# TODO: Find the sum and average of the original numbers
sum_of_numbers = sum(numbers)
average_of_numbers = sum_of_numbers / len(numbers)

# TODO: Print the results
print("sum:", sum_of_numbers)
print("average:", average_of_numbers)

#-------------------------------------------------------------------------
# Question 3: Creating and Modifying Dictionaries

# TODO: Create a dictionary of countries and their capitals
countries_capitals = {"france": "paris" , "egypt": "cairo" , "germany": "berlin" , "japan": "tokyo"}
# TODO: Add a new country-capital pair
countries_capitals["south africa"] = "pretoria"
# TODO: Update the capital of an existing country
countries_capitals["germany"] = "dortmund"
# TODO: Remove a country-capital pair
del countries_capitals["egypt"]
# TODO: Print the modified dictionary
print(countries_capitals)

#-------------------------------------------------------------------------
# Question 4: Dictionary Operations

# TODO: Create a dictionary of fruit colors
fruit_colors = {"watermelon": "red" , "apple": "green"}

# TODO: Print all the fruits (keys)
print(fruit_colors.keys())
# TODO: Print all the colors (values)
print(fruit_colors.values())
# TODO: Print each fruit and its color
for fruit, color in fruit_colors.items():
    print(fruit, ":" , color)
# TODO: Check if a fruit is in the dictionary and print its color
fruit_to_check = "apple"
if fruit_to_check in fruit_colors:
    color = fruit_colors[fruit_to_check]
    print(fruit_to_check, "is" , color)
else:
    print(fruit_to_check, "is not inn the dictionary.")