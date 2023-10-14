
"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Reference:https://www.geeksforgeeks.org/python-program-for-program-for-array-rotation-2/

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""
class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k < len(nums):
            nums[:] = nums[-k:] + nums[:-k]
        else:
            for j in range(k):
                nums[:] = nums[-1:] + nums[:-1]
                
