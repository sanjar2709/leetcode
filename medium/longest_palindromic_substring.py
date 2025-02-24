# 5. Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_palindrome = ""
        for i in range(len(s)):
            palindrome_text1 = self.ExpandAroundCenter(s, i, i)
            palindrome_text2 = self.ExpandAroundCenter(s, i, i + 1)
            if len(max_palindrome) <= len(palindrome_text1):
                max_palindrome = palindrome_text1
            if len(max_palindrome) <= len(palindrome_text2):
                max_palindrome = palindrome_text2

        return max_palindrome

    def ExpandAroundCenter(self, s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left+1:right]



solution = Solution()
result = solution.longestPalindrome(s='babad')
print(result)
