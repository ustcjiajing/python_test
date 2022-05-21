#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 冒泡排序
class Solution(object):
    def bubbleSort(self, arr):
        if len(arr) <= 1:
            return arr
        for i in range(1, len(arr)):
            for j in range(0, len(arr) - i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

if __name__ == "__main__":
    arr = [1,4,9,3,7,5]
    s = Solution()
    print(s.bubbleSort(arr))
