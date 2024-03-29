# Day 20
# Given a string containing a mix of uppercase and lowercase characters, toggle the case of each character (i.e., convert lowercase to uppercase and uppercase to lowercase).

def toggle_case(input_str):
    toggled_str = ""
    for char in input_str:
        if char.islower():
            toggled_str += char.upper()
        elif char.isupper():
            toggled_str += char.lower()
        else:
            toggled_str += char  # Preserve non-alphabetic characters
    return toggled_str

# Take user input
user_input = input("Enter a string: ")
result = toggle_case(user_input)
print("Toggled case:", result)
