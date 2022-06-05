"""
222. 完全二叉树的节点个数
给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。
完全二叉树 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。
输入：root = [1,2,3,4,5,6]
输出：6
"""

# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math

class Solution(object):
    def countNodes(self, root):
        l = r = root
        hl, hr = 0, 0   # 记录左、右子树的高度
        while l is not None:
            l = l.left
            hl += 1
        while r is not None:
            r = r.right
            hr += 1
        # 如果左右子树的高度相同，说明是一颗满二叉树
        if hl == hr:
            return int(math.pow(2, hl)) - 1
        # 如果左右子树高度不同，则按普通二叉树的逻辑计算
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
