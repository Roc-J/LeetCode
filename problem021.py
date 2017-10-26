# -*- coding:utf-8 -*- 
# Author: Roc-J

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val <= l2.val:
            l3 = l1
            if l1.next:
                l1 = l1.next
            else:
                l3.next = l2
                return l3
        else:
            l3 = l2
            if l2.next:
                l2 = l2.next
            else:
                l3.next = l1
                return l3
        root = l3
        while True:
            if l1.val <= l2.val:
                l3.next = l1
                l3 = l3.next
                if l1.next:
                    l1 = l1.next
                else:
                    l3.next = l2
                    break
            else:
                l3.next = l2
                l3 = l3.next
                if l2.next:
                    l2 = l2.next
                else:
                    l3.next = l1
                    break
        return root
