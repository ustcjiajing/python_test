#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Solution(object):
    def insertSort(self, arr):
        if len(arr) <= 1:
            return arr
        for i in range(len(arr)):
            cur = arr[i]
            pre = i - 1
            while pre > 0 and arr[pre] > cur:
                arr[pre+1] = arr[pre]
                pre -= 1
            arr[pre+1] = cur
        return arr


if __name__ == "__main__":
    arr = [1,6,2,3,8,5]
    s = Solution()
    print(s.insertSort(arr))
