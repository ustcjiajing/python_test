"""
34. 在排序数组中查找元素的第一个和最后一个位置
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。
进阶：你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
输入：nums = [], target = 0
输出：[-1,-1]
"""

class Solution(object):
    def getLeftBorder(self, nums, target):
        left, right = 0, len(nums) - 1
        leftBorder = -2    # 记录leftBorder没有被赋值的情况
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:     # 寻找左边界，nums[mid] == target时更新rightBorder
                right = mid - 1
                leftBorder = right
            else:
                left = mid + 1
        return leftBorder
    
    def getRightBorder(self, nums, target):
        left, right = 0, len(nums) - 1
        rightBorder = -2    # 记录rightBorder没有被赋值的情况
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:     
                right = mid - 1
            else:
                left = mid + 1      # 寻找右边界，nums[mid] == target时更新rightBorder
                rightBorder = left
        return rightBorder

    def searchRange(self, nums, target):
        leftBorder = self.getLeftBorder(nums, target)
        rightBorder = self.getRightBorder(nums, target)
        # 情况一:target 在数组范围的右边或者左边，例如数组{3, 4, 5}，target为2或者数组{3, 4, 5},target为6，此时应该返回{-1, -1}

        if leftBorder == -2 or rightBorder == -2:
            return [-1, -1]
        # 情况三:target 在数组范围中，且数组中存在target，例如数组{3,6,7},target为6，此时应该返回{1, 1}
        if rightBorder- leftBorder > 1:
            return [leftBorder + 1, rightBorder - 1]
        # 情况二:target 在数组范围中，且数组中不存在target，例如数组{3,6,7},target为5，此时应该返回{-1, -1}
        return [-1, -1]

    def binarySearch(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1

    def searchRange_1(self, nums, target):
        index = self.binarySearch(nums, target)
        if index == -1:  # nums 中不存在 target，直接返回 {-1, -1}
            return [-1, -1]
        # nums 中存在 target，则左右滑动指针，来找到符合题意的区间
        left, right = index, index
        # 向左滑动，找左边界
        while left - 1 >= 0 and nums[left - 1] == target:
            left -= 1
        # 向右滑动，找右边界
        while right + 1 < len(nums) and nums[right + 1] == target:
            right += 1
        return [left, right]
        
