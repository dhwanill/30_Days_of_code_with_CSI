# Day 24
#6 Write a recursive function to check if a given string is a palindrome

def is_palindrome(s):
    # Base case: an empty string or a string with a single character is a palindrome
    if len(s) <= 1:
        return True
    # Recursive case: check if the first and last characters are equal, then check the rest
    return s[0] == s[-1] and is_palindrome(s[1:-1])

# Get user input for a string
user_input = input("Enter a string: ")

# Convert the input to lowercase to make the palindrome check case-insensitive
user_input = user_input.lower()

# Check if the input string is a palindrome
if is_palindrome(user_input):
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")