"""
240. 搜索二维矩阵 II
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
链接：https://leetcode.cn/problems/search-a-2d-matrix-ii
"""

class Solution(object):
    # 时间复杂度：O(mn)
    # 空间复杂度：O(1)
    def searchMatrix_1(self, matrix, target):
        for row in matrix:
            for item in row:
                if item == target:
                    return True
        return False

    def binary_search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    # 时间复杂度：O(mlogn)
    # 空间复杂度：O(1)
    def searchMatrix_2(self, matrix, target):   
        for row in matrix:
            index = self.binary_search(row, target)
            if index < len(row) and index != -1:
                return True

    # 时间复杂度：O(m+n)
    # 空间复杂度：O(1)
    def searchMatrix(self, matrix, target): 
        m, n = len(matrix), len(matrix[0])
        x, y = 0, n - 1
        while x < m and y >= 0:
            if matrix[x][y] == target:
                return True
            if matrix[x][y] > target:
                y -= 1
            else:
                x += 1
        return False
