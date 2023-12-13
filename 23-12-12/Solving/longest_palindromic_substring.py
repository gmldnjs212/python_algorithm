# https://leetcode.com/problems/longest-palindromic-substring/

class Solution(object):
    def longestPalindrome(self, s):
        long = ""
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                if len(long) >= j-i:
                    continue
                elif s[i:j] == s[i:j][::-1]:
                    long = s[i:j]
        return long

s1 = Solution()
print(s1.longestPalindrome(s = "babad"))
print(s1.longestPalindrome(s = "cbbd"))
