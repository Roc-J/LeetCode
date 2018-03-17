#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

import collections
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        c = collections.Counter(nums)
        for i in c:
            if k > 0 and i + k in c or k == 0 and c[i] > 1:
                result += 1
        return result

if __name__ == '__main__':
    print(Solution().findPairs([1, 3, 1, 5, 4, 4], 0))