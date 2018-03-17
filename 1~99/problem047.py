#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]
        result = []
        for i, num in enumerate(nums):
            n = nums[:i] + nums[i+1:]
            for y in self.permuteUnique(n):
                if [num] + y not in result:
                    result.append([num] + y)
        return result

if __name__ == '__main__':
    print(Solution().permute([1,2,2]))