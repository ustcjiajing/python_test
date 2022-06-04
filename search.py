#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Solution(object):
  def search(self, nums, target):
      left = 0
      right = len(nums) - 1
      while left <= right:
          mid = (left + right) // 2
          if nums[mid] == target:
              return mid
          if nums[mid] > target:
              right = mid - 1
          else:
              left = mid + 1
      return -1
