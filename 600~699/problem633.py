#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

import math

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        maxs = 1
        while (maxs * maxs) < c:
            maxs += 1

        lo = 0
        hi = maxs
        while lo <= hi:
            if ((lo * lo) + (hi * hi)) == c:
                return True
            if ((lo * lo) + (hi * hi)) < c:
                lo += 1
            if ((lo * lo) + (hi * hi)) > c:
                hi -= 1
        return False

if __name__ == '__main__':
    print(Solution().judgeSquareSum(2))