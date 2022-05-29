"""
125. 验证回文串
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。
输入: "A man, a plan, a canal: Panama"
输出: true
解释："amanaplanacanalpanama" 是回文串
"""

class Solution(object):
    # 时间复杂度：O(s)
    # 空间复杂度：O(s)
    def isPalindrome_1(self, s):
        s_new = "".join(ch.lower() for ch in s if ch.isalnum())
        return s_new == s_new[::-1]

    # 时间复杂度：O(s)
    # 空间复杂度：O(s)
    def isPalindrome_2(self, s):
        s_new = "".join(ch.lower() for ch in s if ch.isalnum())
        left, right = 0, len(s_new) - 1
        while left < right:
            if s_new[left] != s_new[right]:
                return False
            left += 1
            right -= 1
        return True

    # 时间复杂度：O(s)
    # 空间复杂度：O(1)
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left < right:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
        return True
