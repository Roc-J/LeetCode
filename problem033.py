#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # if target in nums:
        #     return nums.index(target)
        # else:
        #     return -1
        left, right = 0, len(nums)-1
        mid = 0
        while left <= right:
            mid = left + (right-left)/2
            if nums[mid] == target:
                return mid
            # 转折点在右边
            elif nums[right] < nums[mid]:
                if target>=nums[left] and target <=nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
