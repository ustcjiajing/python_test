#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
@File: reverse_list.py
@Author: jiajing
@Data: 2022/04/26
"""

#给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值 target 的那两个整数，并返回它们的数组下标。

class Solution(object):
    # 时间复杂度：
    # 空间复杂度：
    def twoSum(self, nums, target):
        records = {}
        for index, value in enumerate(nums):
            if target - value not in records:
                records[value] = index
            else:
                return [records[target - value], index]
    # 时间复杂度：
    # 空间复杂度：        
    def twoSum_1(self, nums, target):
        for i in range(0, len(nums)-1):
            for j in  range(i+1, len(nums)-1):
                if nums[i] + nums[j] == target:
                    return [i, j]


if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3,4,8,5]
    target = 9
    res = s.twoSum(nums, target)
    print(res)
