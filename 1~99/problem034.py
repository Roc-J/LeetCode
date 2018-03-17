#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # result = []
        # result.reverse()
        # if target not in nums:
        #     return [-1, -1]
        # else:
        #     result.append(nums.index(target))
        #     result.append(len(nums) - nums[::-1].index(target) - 1)
        #     return result

        # result = []
        # for i in range(len(nums)):
        #     if nums[i] < target:
        #         pass
        #     elif nums[i] == target:
        #         result.append(i)
        #     else:
        #         break
        # if len(result) > 0:
        #     return [min(result), max(result)]
        # else:
        #     return [-1, -1]

        def extreme_insertion_index

if __name__ == '__main__':
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 110))