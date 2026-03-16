"""
1. Two Sum
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices
of the two numbers such that they add up to target.
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            other_num = target - num
            if other_num in seen:
                return [seen[other_num], i]
            seen[num] = i


if __name__ == "__main__":
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    result = s.twoSum(nums, target)
    print(f"Target is {target}, position of two sums is {result}")