# -*- coding:utf-8 -*- 
# Author: Roc-J

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        countA = 0
        rootA = headA
        while rootA != None:
            countA += 1
            if rootA.next:
                rootA = rootA.next
            else:
                break

        countB = 0
        rootB = headB
        while rootB:
            countB += 1
            if rootB.next:
                rootB = rootB.next
            else:
                break

        if countA == 0:
            return None
        if countB == 0:
            return None

        if countA <= countB:
            diff = countB - countA
            while diff > 0:
                if headB.next:
                    headB = headB.next
                    diff -= 1
        else:
            diff = countA - countB
            while diff > 0:
                if headA.next:
                    headA = headA.next
                    diff -= 1

        while headA and headB:
            if headA.val == headB.val:
                return headA
            if headA.next and headB.next:
                headA = headA.next
                headB = headB.next
            else:
                break
        return None
