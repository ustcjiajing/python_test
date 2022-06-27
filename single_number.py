"""
136. 只出现一次的数字
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
说明：你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4

链接：https://leetcode.cn/problems/single-number
"""

class Solution(object):
    def singleNumber(self, nums):
        res = nums[0]
        n = len(nums)
        for i in range(1, n):
                res = res ^ nums[i]
        return res
  
    # 方法2 需要from functools import reduce
    def singleNumber_2(self, nums):
        return reduce(lambda x, y: x ^ y, nums)
      
    
