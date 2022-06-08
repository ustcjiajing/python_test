"""
647. 回文子串
给你一个字符串 s ，请你统计并返回这个字符串中 回文子串 的数目。
回文字符串 是正着读和倒过来读一样的字符串。
子字符串 是字符串中的由连续字符组成的一个序列。
具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。
输入：s = "abc"
输出：3
解释：三个回文子串: "a", "b", "c"
链接：https://leetcode.cn/problems/palindromic-substrings
"""

class Solution(object):
    def countSubstrings(self, s):
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    res += 1
        return res
