#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Solution(object):
    def selectionSort(self, arr):
        if len(arr) <= 1:
            return arr
        for i in range(len(arr)-1):
            minIndex = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[minIndex]:
                    minIndex = j
            if i != minIndex:
                arr[i], arr[minIndex] = arr[minIndex], arr[i]
        return arr


if __name__ == "__main__":
    arr = [1,6,2,3,8,5]
    s = Solution()
    print(s.selectionSort(arr))
