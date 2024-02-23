# Day 22
# Implement a recursive function to compute the nth Fibonacci number.

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Get user input for the desired Fibonacci number
user_input = int(input("Enter the position of the Fibonacci number: "))

# Calculate and print the Fibonacci number
result = fibonacci(user_input)
print(f"The Fibonacci number at position {user_input} is: {result}")