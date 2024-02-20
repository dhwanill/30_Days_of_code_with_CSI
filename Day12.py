# Day 12
# Function to dentify the missing number in an array comprising distinct values from 0 to n, inclusive, with a range spanning 0, 1, 2, ..., 1000.

def find_missing_number(nums):
    # Calculate the expected sum of the first n natural numbers
    n = len(nums) + 1
    expected_sum = (n * (n + 1)) // 2
    
    # Calculate the actual sum of the given array
    actual_sum = sum(nums)
    
    # Find the missing number by subtracting the actual sum from the expected sum
    missing_number = expected_sum - actual_sum
    
    # Return the missing number
    return missing_number

# Example usage:
# Prompt for user input
input_numbers = input("Enter the numbers separated by spaces: ")

# Convert input to a list of integers
numbers = list(map(int, input_numbers.split()))

# Call the find_missing_number function
result = find_missing_number(numbers)

# Output the result
print(f"The missing number is: {result}")
