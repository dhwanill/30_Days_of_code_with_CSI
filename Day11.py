# Day 11 of 30 days of code
#Implement the insertion sort algorithm to sort an array of integers in non-decreasing order.After sorting the array, implement the binary search algorithm to search for a given integer in the sorted array.

def insertion_sort(arr):
    # Sorts the array using Insertion Sort.
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def binary_search(arr, target):
    # Implements Binary Search on a sorted array.
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Target found, return the index
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Target not found

# User input: Entering elements of the array
my_array = list(map(int, input("Enter elements of the array: ").split()))

# User input: Entering the target integer for binary search
target_value = int(input("Enter the integer to search: "))

# Sorting the array using Insertion Sort
insertion_sort(my_array)

# Applying Binary Search on the sorted array
result_index = binary_search(my_array, target_value)

# Displaying the result
if result_index != -1:
    print(f"{target_value} found at index {result_index} in the sorted array.")
else:
    print(f"{target_value} not found in the sorted array.")
