# Day 8 
# Write a program to reverse an array


def reverse_array(arr):
    return arr[::-1]

# user input: Enter elements separated by spaces
user_input = input("Enter elements of the array separated by spaces: ")

# Converting input to a list of integers
my_array = list(map(int, user_input.split()))

# Reversing the array and printing
reversed_array = reverse_array(my_array)
print(f"The reversed array is: {reversed_array}")
