#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
题目：合并两个有序数组
给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。
输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
解释：需要合并 [1,2,3] 和 [2,5,6] 。
合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。
"""

# 方法一：先合并，再排序（先将数组nums2放到nums1的尾部，然后直接对整个数组进行排序）
# 时间复杂度：O((m+n)log(m+n)),排序序列长度为 m+n，套用快速排序的时间复杂度
# 空间复杂度：O(log(m+n)),排序序列长度为 m+n，套用快速排序的时间复杂度
def merge(self, nums1, m, nums2, n):
    nums1[m:] = nums2
    nums1.sort()
  

# 方法二：双指针(将两个数组看作队列，每次从两个数组头部取出比较小的数字放到结果中)
# 时间复杂度：O(m+n),指针移动单调递增，最多移动 m+n次
# 空间复杂度：O(m+n),需要建立长度为 m+n 的中间数组 sorted
def merge(self, nums1, m, nums2, n):
    sorted = []
    p1, p2 = None, None
    while p1 < m or p2 < n:
        if p1 == m:
            sorted.append(nums2[p2])
            p2 += 1
        elif p2 == n:
            sorted.append(nums1[p1])
            p1 += 1
        elif nums1[p1] < nums2[p2]:
            sorted.append(nums1[p1])
            p1 += 1
        else:
            sorted.append(nums2[p2])
            p2 += 1
    nums1[:] = sorted

# 方法三：逆向双指针
# 时间复杂度：O(m+n),指针移动单调递减，最多移动 m+n 次
# 空间复杂度：O(1)
def merge(self, nums1, m, nums2, n):
    p1, p2 = m - 1, n - 1
    tail = m + n - 1
    while p1 >= 0 or p2 >= 0:
        if p1 == -1:
            nums1[tail] = nums2[p2]
            p2 -= 1
        elif p2 == -1:
            nums1[tail] = nums1[p1]
            p1 -= 1
        elif nums1[p1] > nums2[p2]:
            nums1[tail] = nums1[p1]
            p1 -= 1
        else:
            nums1[tail] = nums2[p2]
            p2 -= 1
        tail -= 1
