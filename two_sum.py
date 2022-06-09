#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
@File: reverse_list.py
@Author: jiajing
@Data: 2022/04/26
"""

#给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值 target 的那两个整数，并返回它们的数组下标。

class Solution(object):
    # 时间复杂度：O(n)
    # 空间复杂度：O(n) 
    def twoSum(self, nums, target):
        records = dict()
        for index, value in enumerate(nums):
            if target - value in records:
                return [records[target - value], index]
            records[nums[index] = index                
        return []
             
    # 时间复杂度：O(n2)
    # 空间复杂度：O(1)
    def twoSum_1(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in  range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3,4,8,5]
    target = 9
    res = s.twoSum(nums, target)
    print(res)
