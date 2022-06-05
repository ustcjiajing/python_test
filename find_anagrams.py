"""
438. 找到字符串中所有字母异位词
给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。
输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
"""

class Solution(object):
    def findAnagrams(self, s, p):
        left, right = 0, 0
        match = 0
        window = {}
        needs = dict((i, p.count(i)) for i in p)
        res = []

        while right < len(s):
            c1 = s[right]
            # 更新窗口数据
            if c1 in needs.keys():
                window[c1] = window.get(c1, 0) + 1
                if window[c1] == needs[c1]:
                    match += 1
            right += 1

            # 判断左窗口是否需要收缩
            while match == len(needs):
                # 当窗口符合条件，把起始索引加入res
                if right - left == len(p):
                    res.append(left)
                c2 = s[left]
                left += 1
                # 更新窗口数据
                if c2 in needs.keys():
                    window[c2] -= 1
                    if window[c2] < needs[c2]:
                        match -= 1
        return res
