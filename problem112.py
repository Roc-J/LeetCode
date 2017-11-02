# -*- coding:utf-8 -*- 
# Author: Roc-J

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        nodelist = [root]
        while True:
            result = []
            for item in nodelist:
                if item.left == None and item.right == None:
                    if item.val == sum:
                        return True
                if item.left:
                    item.left.val += item.val
                    result.append(item.left)
                if item.right:
                    item.right.val += item.val
                    result.append(item.right)
            if len(result) == 0:
                break
            nodelist = result
        return False