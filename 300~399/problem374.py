# -*- coding:utf-8 -*- 
# Author: Roc-J

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        while low <= high:
            mid = (low + high)/2
            value = guess(mid)
            if value == -1:
                high = mid -1
            elif value == 1:
                low = mid + 1
            else:
                return mid