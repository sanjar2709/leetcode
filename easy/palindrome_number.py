# 9. Palindrome Number
# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution(object):
    def isPalindrome(self, x: int) -> bool:
        if x <= 0:
            return False

        number = x
        s = 0
        while number > 0:
            rest = number % 10
            s = s * 10 + rest
            number //= 10
        return x == s


solution = Solution()
result = solution.isPalindrome(101)

print(result)