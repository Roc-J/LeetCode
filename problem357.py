#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        result = [10, 9*9]
        for i in range(9):
            result.append(result[-1]*(8-i))
        return sum(result[:n])

if __name__ =='__main__':
    print(Solution().countNumbersWithUniqueDigits(3))