# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
#
# Given a string s, return true if it is a palindrome, or false otherwise.
#
# A palindrome is a string that reads the same forward and backward after:
# - Converting all uppercase letters to lowercase
# - Removing all non-alphanumeric characters


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while( left < right):
            while(left < right and not s[left].isalnum()):
                left += 1 
            while(left < right and not s[right].isalnum()):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True

if __name__ == "__main__":
    solution = Solution()
    s = "A man, a plan, a canal: Panama"
    print(f"s = {s} is a palindrome: { solution.isPalindrome( s ) }")