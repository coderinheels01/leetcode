"""
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together.
You can return the answer in any order.
"""

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        frequency = defaultdict(list)

        for s in strs:
            frequency[tuple(sorted(s))].append(s)

        return list(frequency.values())

if __name__ == "__main__":
    s = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(f"annagram list original {strs} and result is {s.groupAnagrams(strs)}")
