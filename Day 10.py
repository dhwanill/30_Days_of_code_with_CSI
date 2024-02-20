# Day 10 of 30 days of code
# Implement bubble sort algorithm to sort an array

def bubble_sort(arr):
    # Getting the length of the array
    n = len(arr)

    # Iterating through the array elements
    for i in range(n):
        # Comparing and swapping adjacent elements
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swapping elements if the condition is met
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# User input: Entering elements of the array
user_input = input("Enter elements of the array separated by spaces: ")

# Converting input to a list of integers
my_array = list(map(int, user_input.split()))

# Performing bubble sort
bubble_sort(my_array)

# Displaying the sorted array
print("Sorted Array:", my_array)
