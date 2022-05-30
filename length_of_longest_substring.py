"""
3. 无重复字符的最长子串
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
"""

class Solution(object):        
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        max_len, hashset = 0, set()
        left, right = 0, 0
        n = len(s)

        for i in range(n):
            right += 1
            while s[i] in hashset:
                hashset.remove(s[left])
                left += 1
                right -= 1
            if right > max_len:
                max_len = right
            hashset.add(s[i])
        return max_len
