"""
5. 最长回文子串
给你一个字符串 s，找到 s 中最长的回文子串。
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
https://leetcode.cn/problems/longest-palindromic-substring/
"""

class Solution(object):
    def Palindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1 : r]

    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            s1 = self.Palindrome(s, i, i)
            s2 = self.Palindrome(s, i, i + 1)
            if len(res) <= len(s1):
                res = s1
            if len(res) <= len(s2):
                res = s2
        return res
