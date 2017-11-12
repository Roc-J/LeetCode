# -*- coding:utf-8 -*- 
# Author: Roc-J

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        result = []
        while head:
            result.append(head.val)
            head = head.next
        for i in range(len(result)/2):
            if result[i] == result[-(i+1)]:
                continue
            else:
                return False
        return True

