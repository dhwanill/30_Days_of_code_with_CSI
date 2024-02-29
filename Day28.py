# Day 28
# Converting a Roman numeral to an integer.

def roman_to_integer(s: str) -> int:
    # Creating a dictionary to map Roman numerals to their integer values
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    result = 0  # Storing the final integer result
    prev_value = 0  # Keeping track of the previous value
    
    # Iterating through the input Roman numeral in reverse order
    for char in s[::-1]:
        current_value = roman_dict[char]
        
        # Checking if the current value is greater than or equal to the previous value
        if current_value >= prev_value:
            result += current_value
        else:
            result -= current_value
        
        prev_value = current_value
    
    return result

# Taking input during execution
roman_numeral = input("Enter a Roman numeral: ")
integer_value = roman_to_integer(roman_numeral.upper())
print(f"Integer value: {integer_value}")