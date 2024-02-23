# Day 23
# Write a recursive function to calculate the sum of digits of a positive integer.

def sum_of_digits(n):
    # Base case: if the number is a single digit, return the number itself
    if n < 10:
        return n
    else:
        # Recursive case: sum the last digit and call the function with the remaining digits
        return n % 10 + sum_of_digits(n // 10)

# Get user input for a positive integer
user_input = int(input("Enter a positive integer: "))

# Check if the input is a positive integer
if user_input <= 0:
    print("Please enter a positive integer.")
else:
    # Calculate and print the sum of digits
    result = sum_of_digits(user_input)
    print(f"The sum of digits of {user_input} is: {result}")