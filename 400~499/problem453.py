#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 0
        while True:
            max1, min1 = max(nums), min(nums)
            if max1 == min1:
                break
            diff = max1 - min1
            idx, c = nums.index(max1), c + diff
            for i in range(len(nums)):
                nums[i] = nums[i] + diff if i != idx else nums[i]

        return c
        # return sum(nums) - len(nums) * min(nums)


if __name__ == '__main__':
    print(Solution().minMoves([1,2147483647]))