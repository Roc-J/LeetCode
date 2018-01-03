#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: qjk

import sys
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        size = len(nums)
        ans = []
        if size <= 2:
            return ans
        nums.sort()
        i = 0
        distance = sys.maxint
        for i in range(size-2):
            j = i + 1
            k = size - 1
            while j < k:
                count = nums[i] + nums[j] + nums[k]
                diff = abs(count - target)
                if diff < distance:
                    distance = diff
                    result = count
                if count < target:
                    j += 1
                else:
                    k -= 1
        return result

if __name__ == '__main__':
    print(Solution().threeSumClosest([1,1,-1,-1,3], -1))