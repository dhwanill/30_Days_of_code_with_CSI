#Day 13
# Function that takes an array of integers as input and calculates the maximum, minimum, sum, and average of the elements in the array

def calculate_statistics(arr):
    if not arr:
        return None
    
    maximum = max(arr)
    minimum = min(arr)
    total_sum = sum(arr)
    average = total_sum / len(arr)

    return maximum, minimum, total_sum, average

# User input
user_input = input("Enter space-separated integers: ")
array_of_integers = list(map(int, user_input.split()))

# Calculate and print statistics
result = calculate_statistics(array_of_integers)
print("Maximum:", result[0])
print("Minimum:", result[1])
print("Sum:", result[2])
print("Average:", result[3])
