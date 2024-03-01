# Day 29
# Determine if a given string of parentheses is valid.

def isValid(s: str) -> bool:
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}'}

    for char in s:
        if char in brackets.keys():
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False

    return not stack

# Taking Input
input_string = input("Enter a string of parentheses: ")
result = isValid(input_string)

if result:
    print("The given string of parentheses is valid.")
else:
    print("The given string of parentheses is not valid.")