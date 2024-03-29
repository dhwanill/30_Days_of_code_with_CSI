# Day 9
# Implementing a linear search algorithm to find an element in an array.

def linear_search(arr, target):
    for position, element in enumerate(arr):
        if element == target:
            return position  # Return the position if the target is found
    return 0  # Return 0 if the target is not found

# User input: Enter space-separated elements of the array
user_input = input("Enter space-separated elements of the array: ")

# Converting input to a list of integers
my_array = list(map(int, user_input.split()))

# User input: Enter the target element to search
target_element = int(input("Enter the target element to search: "))

# Performing linear search and print the result
result = linear_search(my_array, target_element)
if result:
    print(f"Element {target_element} found at position {result}.")
else:
    print(f"Element {target_element} not found in the array.")
