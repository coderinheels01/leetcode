"""
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s,
and false otherwise.
"""

from collections import Counter

class Solution:
    def isAnagram1(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        frequency = {}

        for c in s:
            frequency[c] = frequency.get(c, 0) + 1

        for c in t:
            frequency[c] = frequency.get(c, 0) - 1

        return all(v == 0 for v in frequency.values())

    def isAnagram2(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        
    def isAnagram3(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        frequency = {}

        for a,b in zip(s, t):
            frequency[a] = frequency.get(a, 0) + 1
            frequency[b] = frequency.get(b, 0) - 1

        return all(v == 0 for v in frequency.values())

if __name__ == "__main__":
    s = Solution()
    s1 = "anagram"
    s2 = "nagaram"
    print(f"string s{s1} and string t{s2} are anagrams {s.isAnagram1(s1, s2)}")
    print(f"string s{s1} and string t{s2} are anagrams {s.isAnagram2(s1, s2)}")
    print(f"string s{s1} and string t{s2} are anagrams {s.isAnagram3(s1, s2)}")