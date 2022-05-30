"""
102. 二叉树的层序遍历
给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]
"""

# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # 时间复杂度：O(n)
    # 空间复杂度：O(n)
    def levelOrder(self, root):
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            # 获取当前队列的长度，这个长度相当于 当前这一层的节点个数
	    size = len(queue)
       	    level = []
            # 将队列中的元素都拿出来(也就是获取这一层的节点)，放到临时list中
	    # 如果节点的左/右子树不为空，也放入队列中
	    for _ in range(size):
	        node = queue.pop(0)
		level.append(node.val)
		if node.left:
		    queue.append(node.left)
		if node.right:
		    queue.append(node.right)
	    # 将临时list加入最终返回结果中
	    res.append(level)
        return res
