# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without duplicate characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_list = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_list:
                char_list.remove(s[left])
                left += 1

            char_list.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length


solution = Solution()
result = solution.lengthOfLongestSubstring('pwwkew')
print(result)
