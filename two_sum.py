#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值 target 的那两个整数，并返回它们的数组下标。

class Solution(object):
    """
    """
    def twoSum(self, nums, target):
        """
        """
        records = {}
        for index, value in enumerate(nums):
            if target - value not in records:
                records[value] = index
            else:
                return [records[target - value], index]


if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3,4,8,5]
    target = 9
    res = s.twoSum(nums, target)
    print(res)
