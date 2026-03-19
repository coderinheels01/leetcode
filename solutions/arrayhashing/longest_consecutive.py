"""
128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest
consecutive sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
    Input: nums = [100, 4, 200, 1, 3, 2]
    Output: 4
    Explanation: The longest consecutive sequence is [1, 2, 3, 4]. Its length is 4.

Example 2:
    Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    Output: 9

Constraints:
    - 0 <= nums.length <= 10^5
    - -10^9 <= nums[i] <= 10^9
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        longestConsecutive = 0;

        for num in nums:
            current_len = 1
            if num-1 not in unique:
                while(num+current_len in unique):
                    current_len += 1
                
            longestConsecutive = max(current_len , longestConsecutive)

        return longestConsecutive

if __name__ == "__main__":
    sol = Solution()

    # Example 1
    nums1 = [100, 4, 200, 1, 3, 2]
    print(f"Input: {nums1}")
    print(f"Output: {sol.longestConsecutive(nums1)}")  # Expected: 4

    # Example 2
    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(f"Input: {nums2}")
    print(f"Output: {sol.longestConsecutive(nums2)}")  # Expected: 9