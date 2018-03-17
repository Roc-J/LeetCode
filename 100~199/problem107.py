# -*- coding:utf-8 -*-
# Author: Roc-J

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def get_value_node(self, nodelist):
        node = []
        result = []
        for item in nodelist:
            result.append(item.val)
            if item.left:
                node.append(item.left)
            if item.right:
                node.append(item.right)
        return node, result

    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        begin = [root]
        result = []
        node, item = self.get_value_node(begin)
        result.insert(0, item)
        while len(node)>0:
            node, item = self.get_value_node(node)
            result.insert(0, item)

        return result

