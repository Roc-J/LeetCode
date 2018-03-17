#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        for i in range(1, len(nums)+2):
            if i not in nums:
                return i



if __name__ == '__main__':
    print(Solution().firstMissingPositive([1,2,3]))