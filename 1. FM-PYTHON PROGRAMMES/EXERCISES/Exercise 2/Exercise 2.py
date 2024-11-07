# Question 1: Arithmetic and Assignment Operators

# TODO: Add 3 to x using the += operator
x = 13
x += 3 
print(x)

# TODO: Multiply y by 2 using the *= operator
y = 4
y *= 2
print(y)

# TODO: Divide x by y and store the result in a variable called 'result'
result = x // y
print(result)


# TODO: Print the value of 'result'
print(result)
#------------------------------------------------------------------------------------
# Question 2: Comparison and Logical Operators

# TODO: Create a condition that checks if a is greater than b
a = 5
b = 2
if a > b: 
    print("is greater than b")
else:
    print("a is less than or equal to b ") 



# TODO: Create a condition that checks if b is even (hint: use the modulus operator)
if b % 2 == 9:
    print("b is even")
else:print("b is odd")
# TODO: Create a condition that checks if c is less than or equal to a
c = 7
if c <= a:
    print("c is less or equal to a")
# else:
    print("c is greater than a")
    
# TODO: Combine the above conditions using logical operators to create a 'final_condition'
#       The 'final_condition' should be True if either:
#       - a is greater than b, or
#       - b is even and c is less than or equal to a
# conditions = a > b or ( b % 5 == 9 or c <= a)
# TODO: Print the value of 'final_condition'
if conditions:
    print(f"a is greater than b , b is even , c is less than or equal to a: {conditions}")
else:
    print("conditions not met")

#------------------------------------------------------------------------------------
# Question 3: Conditional Statements

# TODO: Ask the user to input a test score (0-100) and store it in a variable called 'score'
# score = int(input("enter your test score (0-100): "))
# TODO: Implement a grading system using if-elif-else statements:
#       90-100: A
#       80-89: B
#       70-79: C
#       60-69: D
#       Below 60: F
if 90 <= score <= 100:
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 70 <= score <= 79:
    print("C")
elif 60 <= score <= 69:
    print("D")
else:
    print("F")
# TODO: Print the grade for the given score
print(f" grade for the given score is: {score}")
#------------------------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals

# TODO: Ask the user to input two numbers and store them in variables 'num1' and 'num2'
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# TODO: Ask the user to input an operation (+, -, *, /) and store it in a variable called 'operation'
operation = input("Enter an operation (+, -, *, /): ")
# TODO: Use conditional statements to perform the chosen operation on num1 and num2
if operation == "+": 
   total = num1 + num2
   print(total)
# TODO: Handle the case of division by zero
elif operation == "-":
     total = num1 - num2 
     print(total)
elif operation == "*":
    total = num1 * num2
    print(total)
elif operation == "/":
    if num2 != 0 :
     total = num1 / num2
    else:
     print("error: Division by zero is not allowed ")


# TODO: Print the result of the operation
print(f"results of the operation: {total}")