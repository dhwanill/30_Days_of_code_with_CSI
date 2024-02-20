# Day 4 
# Define a function that calculates the factorial of a given number and use it to find the factorial of 5.


def calculate_factorial(number):
    """
    Calculates the factorial of a given number using recursion.
    
    Parameters:
    - number (int): The number for which to calculate the factorial.
    
    Returns:
    - int: The factorial of the given number.
    """
    # Base case: factorial of 0 or 1 is 1
    if number == 0 or number == 1:
        return 1
    else:
        # Recursive case: multiply the current number by the factorial of (number - 1)
        return number * calculate_factorial(number - 1)

def main():
    # Find the factorial of 5
    result = calculate_factorial(5)
    # Print the result
    print(f"The factorial of 5 is: {result}")

if __name__ == "__main__":
    # Execute the main function if the script is run directly
    main()
