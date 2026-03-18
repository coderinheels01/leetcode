"""
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer such that answer[i]
is equal to the product of all the elements of nums except nums[i].

You must write an algorithm that runs in O(n) time and without using
the division operation.
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = 1
        result = [0] * len(nums)
        
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        postfix = 1

        for i in range(len(nums)-1 , -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([1, 2, 3, 4]))       # [24, 12, 8, 6]
    print(s.productExceptSelf([-1, 1, 0, -3, 3]))   # [0, 0, 9, 0, 0]
