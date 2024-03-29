# Day 17
# Given a string, remove duplicate characters and return

def remove_duplicates(input_string):
    # Use a set to keep track of unique characters
    unique_chars = set()

    # Initialize an empty string to store the result
    result_string = ""

    for char in input_string:
        # Check if the character is not in the set (not a duplicate)
        if char not in unique_chars:
            # Add the character to the set and result string
            unique_chars.add(char)
            result_string += char

    return result_string

# Take input from the user
user_input = input("Enter a string: ")

# Call the function with user input
result = remove_duplicates(user_input)

# Display the results
print(f"Original String: {user_input}")
print(f"String after removing duplicates: {result}")
