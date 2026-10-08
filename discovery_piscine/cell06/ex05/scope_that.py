#!/usr/bin/env python3

def add_one(param):
    param += 1

# Initialize a variable in the body of the program
my_variable = 42

# Display the variable before calling the method
print(my_variable)

# Call the method that adds 1
add_one(my_variable)

# Display the variable again to see the result of variable scope
print(my_variable)
