# Day 21
# Write a recursive function to calculate the factorial of a given non-negative integer.

def calculate_factorial(n):
    """
    Recursive function to calculate the factorial of a given non-negative integer
    
    Args:
    - n (int): Non-negative integer for which factorial is calculated
    
    Returns:
    - int: Factorial of the input integer
    """
    if n < 0:
        return "Factorial is undefined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        # Recursive call to calculate factorial
        return n * calculate_factorial(n - 1)

# Taking input from the user
num = int(input("Enter a non-negative integer: "))
result = calculate_factorial(num)
print(f"The factorial of {num} is: {result}")