# Day 3
# Writing a program that checks if a number entered by the user is even or odd and prints the result.

# User input for a number
number = int(input("Enter a number: "))

# Check if the number is even or odd
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")
