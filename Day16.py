# Day 16
# Given a string, reverse the characters in the string

# A string is a sequence of characters, typically used to represent text, and is enclosed in single (' ') or double (" ") quotes in programming


def reverse_string(input_str):
    return input_str[::-1]

# Take user input
user_input = input("Enter a string: ")

# Reverse the input string
reversed_string = reverse_string(user_input)

# Display the reversed string
print("Reversed string:", reversed_string)
