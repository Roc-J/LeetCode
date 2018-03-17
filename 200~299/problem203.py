# -*- coding:utf-8 -*- 
# Author: Roc-J

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return None
        while head.val == val:
            if head.next:
                head = head.next
            else:
                return None
        root = head
        while head.next:
            if head.next.val == val:
                if head.next.next:
                    head.next = head.next.next
                else:
                    head.next = None
                    return root
            else:
                head = head.next

        return root