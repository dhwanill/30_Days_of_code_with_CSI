# Day 7
# Write a program to find the sum of all elements in an array.

# User input: Enter numbers separated by spaces
user_input = input("Enter numbers separated by spaces: ")

# Convert input to a list of integers and calculate the sum
array_sum = sum(map(int, user_input.split()))

# Print the sum of the numbers
print(f"The sum of your numbers is: {array_sum}")
