"""
217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least
twice in the array, and return false if every element is distinct.
"""


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums));

if __name__ == "__main__":
    s  = Solution()
    nums = [ 1, 2, 3, 1 ]
    print(f"nums = {nums} contains duplicate ? {s.containsDuplicate(nums)}")
    nums = [ 1, 2, 3, 4 ]
    print(f"nums = {nums} contains duplicate ? {s.containsDuplicate(nums)}")
    nums = [ 1,1,1,3,3,4,3,2,4,2 ]
    print(f"nums = {nums} contains duplicate ? {s.containsDuplicate(nums)}")