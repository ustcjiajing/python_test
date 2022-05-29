#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
215. 数组中的第K个最大元素
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
"""

# 方法一：快排
# 时间复杂度：O(nlogn)
# 空间复杂度：O(1)
class Solution(object):
    def quickSort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        lesser = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return self.quickSort(lesser) + [pivot] + self.quickSort(greater)

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.quickSort(nums)
        return nums[len(nums)-k]
        

# 方法一：快速选择（在快排基础上的）优化
# 时间复杂度：O(nlogn)
# 空间复杂度：O(1)
