#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""    
快速排序使用的是分治法（D&C)
（1）找出基线条件（这种条件尽可能简单）
（2）不断将问题分解（缩小问题规模），直到符合基准条件
快速排序算法的性能高度依赖选择的基准值，平均情况O(nlogn)，快排是最快的排序算法之一
"""

class Solution(object):
    def quickSort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        lesser = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return self.quickSort(lesser) + [pivot] + self.quickSort(greater)


if __name__ == "__main__":
    arr = [1,6,2,3,8,5]
    s = Solution()
    print(s.quickSort(arr))
