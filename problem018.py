#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        dict = {}
        if len(nums) < 4:
            return result
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                val = nums[i] + nums[j]
                if val not in dict:
                    dict[val] = [[i, j]]
                else:
                    dict[val].append([i, j])
        for i in range(len(nums)):
            for j in range(i+1, len(nums)-2):
                diff = target - nums[i] - nums[j]
                if diff in dict:
                    for k in dict[diff]:
                        if k[0] > j and [nums[i], nums[j], nums[k[0]], nums[k[1]]] not in result:
                            result.append([nums[i], nums[j], nums[k[0]], nums[k[1]]])

        return result

if __name__ == '__main__':
    print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))