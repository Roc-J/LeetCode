#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None:
            return None
        else:
            count = 1
        pre = head
        root = head
        while pre:
            if pre.next:
                pre = pre.next
                count += 1
            else:
                break
        step = count - n - 1
        while head:
            if step == -1:
                return head.next
            if step == 0:
                head.next = head.next.next
                break
            head = head.next
            step -= 1
        return root