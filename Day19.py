# Day 19
# Given a string, the task is to find the index of the first non-repeating character in it. If there is no such character, the function should return -1

def first_non_repeating_char(s):
    char_count = {}
    
    # Count occurrences of each character
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Find the first non-repeating character
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i
    
    # If no non-repeating character is found
    return -1

# Take input from the user
input_string = input("Enter a string: ")
result = first_non_repeating_char(input_string)

# Display the result
print("Index of the first non-repeating character:", result)
