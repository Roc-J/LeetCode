# -*- coding:utf-8 -*- 
# Author: Roc-J

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generate(self, nums, low, high):
        if low == high:
            return TreeNode(nums[low])
        if low > high:
            return None
        mid = (low + high)/2
        node = TreeNode(nums[mid])
        node.left = self.generate(nums, low, mid-1)
        node.right = self.generate(nums, mid+1, high)
        return node


    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        low, high = 0, len(nums) - 1
        mid = (low + high) / 2
        root = TreeNode(nums[mid])
        root.left = self.generate(nums, low, mid-1)
        root.right = self.generate(nums, mid+1, high)
        return root