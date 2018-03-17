# -*- coding:utf-8 -*- 
# Author: Roc-J

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = 0
        if root:
            left, right = root.left, root.right
            if left and (left.left or left.right) is None:
                result += left.val
            result += self.sumOfLeftLeaves(left) + self.sumOfLeftLeaves(right)
        return result

