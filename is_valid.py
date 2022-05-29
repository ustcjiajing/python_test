#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
  左括号必须用相同类型的右括号闭合。
  左括号必须以正确的顺序闭合。
输入：s = "()"
输出：true
"""

# 栈
# 时间复杂度：O(n)
# 空间复杂度：O(n+∣Σ∣)，其中Σ表示字符集，本题中字符串只包含 66 种括号，∣Σ∣=6。栈中的字符数量为 O(n)，而哈希表使用的空间为O(∣Σ∣)，相加即可得到总空间复杂度
class Solution:
    def isValid(self, s):
        if len(s) % 2 == 1:
            return False
        
        pairs = {            # 用一个哈希表存储每一种括号。哈希表的键为右括号，值为相同类型的左括号。
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = list()
        for item in s:
            if item in pairs:
                if not stack or stack[-1] != pairs[item]:
                    return False
                stack.pop()
            else:
                stack.append(item)
        
        return not stack
