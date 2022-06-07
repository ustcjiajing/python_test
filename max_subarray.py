"""
剑指 Offer 42. 连续子数组的最大和
输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度为O(n)。
输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
https://leetcode.cn/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/
"""

class Solution(object):
    # 时间复杂度：O(n)
    # 空间复杂度：O(n)
    def maxSubArray(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        
        for i in range(1, n):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])
       
        res = nums[0]
        for i in range(0, n):
            res = max(res, dp[i])
        
        return res
