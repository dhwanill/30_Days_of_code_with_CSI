#Day 14
#Given an array of integers and a target element, count the number of occurrences of the target element in the array.

def count_occurrences(arr, target):
    return arr.count(target)

# Input from the user
try:
    num_elements = int(input("Enter the number of elements in the array: "))
    my_array = [int(input("Enter an element: ")) for _ in range(num_elements)]
    target_element = int(input("Enter the target element: "))
    
    # Calculate occurrences
    result = count_occurrences(my_array, target_element)
    print(f"Occurrences of {target_element} in the array: {result}")
except ValueError:
    print("Please enter valid integers for array elements and the target.")
