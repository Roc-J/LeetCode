# -*- coding:utf-8 -*- 
# Author: Roc-J

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        if head == None or head.next == None:
            return head

        pre = head
        cur = head.next
        root = pre
        while cur != None:
            if cur.val != pre.val:
                pre = cur
                cur = cur.next
                continue

            while cur.next != None and cur.next.val == pre.val:
                cur = cur.next

            pre.next = cur.next
            cur = pre.next

        return root
