"""
367. 有效的完全平方数
给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。
进阶：不要 使用任何内置的库函数，如  sqrt 。
输入：num = 16
输出：true
输入：num = 14
输出：false
"""

class Solution(object):
    #时间复杂度：O(logn)
    #空间复杂度：O(1)
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left, right = 0, num
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == num:
                return True
            if mid * mid > num:
                right = mid - 1
            else:
                left = mid + 1
        return False
