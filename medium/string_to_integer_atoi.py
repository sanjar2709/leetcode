# 8. String to Integer (atoi)

class Solution:
    def myAtoi(self, s: str) -> int:
        sent = 1
        response = 0
        index = 0

        while index < len(s) and s[index] == ' ':
            index += 1

        if index < len(s) and (s[index] == '-' or s[index] == '+'):
            if s[index] == '-':
                sent = -1
            index += 1

        while index < len(s) and '0' <= s[index] <= '9':
            response = response * 10 + (ord(s[index]) - ord('0'))
            if response > (2**32 - 1):
                return 2**32 - 1 if sent == 1 else -2**32

            index += 1
        return response * sent


solution = Solution()
result = solution.myAtoi("  42")

print(result)
