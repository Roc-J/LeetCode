# -*- coding:utf-8 -*- 
# Author: Roc-J

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getDepth(self, root):
        if root is None:
            return 0
        ldepth = self.getDepth(root.left)
        rdepth = self.getDepth(root.right)
        if ldepth < rdepth:
            return rdepth+1
        else:
            return ldepth+1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        ldepth = self.getDepth(root.left)
        rdepth = self.getDepth(root.right)

        if abs(ldepth-rdepth) >= 2:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
