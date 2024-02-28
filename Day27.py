# Day 27
# Longest Substring Without Repeating Characters: Find the length of the longest substring without repeating characters.

def longest_substring_details(s: str):
    char_index_map = {}  
    # keeps track of the index of characters
    
    start = 0  
    # starting index of the current substring
    
    max_length = 0  
    # length of the longest substring

    for i, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1

        char_index_map[char] = i

        current_length = i - start + 1

        if current_length > max_length:
            max_length = current_length
            longest_substring = s[start:i + 1]

    return max_length, longest_substring


# Input is taken during execution

input_string = input("Enter a string: ")
length, substring = longest_substring_details(input_string)
print(f"Length of the longest substring without repeating characters: {length}")
print(f"Longest substring without repeating characters: {substring}")