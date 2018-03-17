# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0:
            return False
        if num == 1:
            return True
        if num == 0 or num % 4 > 0:
            return False

        while num > 1:
            r = num % 4
            if r > 0:
                return False
            num = num/4
        return True