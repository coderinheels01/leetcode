# 15. 3Sum
# https://leetcode.com/problems/3sum/
#
# Given an integer array nums, return all the unique triplets
# [nums[i], nums[j], nums[k]] such that:
# - i != j, i != k, and j != k
# - nums[i] + nums[j] + nums[k] == 0
#
# The solution set must not contain duplicate triplets.


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        three_sum_array = []

        for left in range(len(nums)):
            left1 = left + 1
            right1 = len(nums)-1

            if left > 0 and nums[left-1] == nums[left]:
                continue
            while( left1 < right1 ):
                total = nums[left] + nums[left1] + nums[right1]
                if total == 0:
                   three_sum_array.append([nums[left], nums[left1], nums[right1]])
                   while left1 < right1 and nums[left1] == nums[left1+1]:
                        left1 += 1
                   while left1 < right1 and nums[right1] == nums[right1 -1]:
                        right1 -= 1
                   left1 += 1 
                   right1 -= 1
                elif total < 0:
                   left1 += 1
                elif total > 0:
                   right1 -= 1
                
            left += 1
            
        return three_sum_array

if __name__ == "__main__":
    s = Solution()
    nums = [1,2,0,1,0,0,0,0]
    print(f"three sums for array - {nums} is {s.threeSum(nums)}")
    nums = [-100,-70,-60,110,120,130,160]
    print(f"three sums for array - {nums} is {s.threeSum(nums)}")
    nums = [-1,0,1,2,-1,-4]
    print(f"three sums for array - {nums} is {s.threeSum(nums)}")
    nums = [0, 0, 0, 0]
    print(f"three sums for array - {nums} is {s.threeSum(nums)}")


