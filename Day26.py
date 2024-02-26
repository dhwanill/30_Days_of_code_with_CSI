# Day 26
# Two Sum Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to targe, You may assume that each input would have exactly one solution,and you may not use the same element twice. You can return the answer in any order.

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  
# Dictionary to store {val: index} pairs
        for i, n in enumerate(nums):
            diff = target - n  
# Calculating the difference needed to reach the target
            if diff in prevMap:  
# Checking if the needed difference is in the dictionary
                return [prevMap[diff], i]  # If found, return the indices
            prevMap[n] = i  
# Adding the current number to the dictionary with its index
        return []  
# Returning an empty list if no solution is found

# Getting Input from the user during execution
nums = list(map(int, input("Enter the array of integers separated by space: ").split()))
target = int(input("Enter the target sum: "))

solution_instance = Solution()
result = solution_instance.twoSum(nums, target)

if result:
    print(f"Indices of two numbers whose sum is {target}: {result}")
else:
    print("No solution found.")