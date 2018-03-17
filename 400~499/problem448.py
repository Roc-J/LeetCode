#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

'''
正负号标记法
其实具体原理我还没懂
Ｍａｒｋ一下
'''


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for item in nums:
            nums[abs(item)-1] = -abs(nums[abs(item)-1])
        return [i+1 for i, n in enumerate(nums) if n > 0]

if __name__ == '__main__':
    print(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))