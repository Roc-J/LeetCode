# -*- coding:utf-8 -*- 
# Author: Roc-J

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        nodelist = [root]
        depth = 1
        flag = 0
        while True:
            result = []
            for item in nodelist:
                if item.left == None and item.right == None:
                    flag = 1
                    break
                if item.left:
                    result.append(item.left)
                if item.right:
                    result.append(item.right)
            if flag == 1:
                depth += 1
                break
            nodelist = result
            depth += 1
        return depth


