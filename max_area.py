# 11. 盛最多水的容器
# https://leetcode.cn/problems/container-with-most-water/

class Solution(object):
    def maxArea(self, height):
        # 双指针（O(n)，O(1))
        left, right = 0, len(height) - 1
        res = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            res = max(res, area)
            if height[left] <= height[right]:
                l += 1
            else:
                r -= 1
        return res
