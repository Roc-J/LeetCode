#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getValue(self, root):
        return root.val

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nums = []
