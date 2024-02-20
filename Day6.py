# Day 6
# Program to print all elements in an array

# An array is a data structure that stores a collection of elements, each identified by an index or a key. In Python, lists are a versatile type of array where elements can be of different types 

def print_array_elements(arr):
    for element in arr:
        print(element, end=' ')

if __name__ == "__main__":
    # User input: Enter elements separated by spaces
    user_input = input("Enter elements separated by spaces: ")

    # Convert input to a list of integers
    arr = list(map(int, user_input.split()))

    # Print all elements in the array
    print("Array elements:", end=' ')
    print_array_elements(arr)
