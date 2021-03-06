"""
27. 移除元素
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
输入：nums = [3,2,2,3], val = 3
输出：2, nums = [2,2]
输入：nums = [0,1,2,2,3,0,4,2], val = 2
输出：5, nums = [0,1,4,0,3]
"""

# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution(object):
    def removeElement(self, nums, val):
        left, right = 0, 0
        for i in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
            right += 1
        return left
