# Day 15
# Given an array, rotate the array to the right by k steps, where k is non-negative.

def rotate_array(nums, k):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]

# Take input from the user
arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))
k = int(input("Enter the number of steps to rotate to the right: "))

rotate_array(arr, k)
print("Rotated array:", arr)
