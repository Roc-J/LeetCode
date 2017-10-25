# -*- coding:utf-8 -*- 
# Author: Roc-J

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(0)
        root = l3
        c = 0
        value = l1.val + l2.val + c
        if value > 9:
            l3.val += value % 10
            c = 1
        else:
            l3.val += value
            c = 0

        while l1.next and l2.next:
            l1 = l1.next
            l2 = l2.next

            l3.next = ListNode(0)
            l3 = l3.next

            value = l1.val + l2.val + c
            if value > 9:
                l3.val = value % 10
                c = 1
            else:
                l3.val = value
                c = 0

        while l1.next:
            l1 = l1.next

            l3.next = ListNode(0)
            l3 = l3.next

            value = l1.val + c
            if value > 9:
                l3.val = value % 10
                c = 1
            else:
                l3.val = value
                c = 0

        while l2.next:
            l2 = l2.next
            l3.next = ListNode(0)
            l3 = l3.next
            value = l2.val + c
            if value > 9:
                l3.val = value % 10
                c = 1
            else:
                l3.val = value
                c = 0

        if c == 1:
            l3.next = ListNode(c)
        return root



