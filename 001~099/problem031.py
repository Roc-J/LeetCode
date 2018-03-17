#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution(object):
    '''
    求排列的下一个
    １．　求第一个左<右的序列index1
    ２．　求第一个从右数大于这个index１的数，index2，交换这两个数
    ３．index1后的数，从小排序

    '''
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        for x in range(size - 1, -1, -1):
            if nums[x - 1] < nums[x]:
                break
        if x > 0:
            for y in range(size - 1, -1, -1):
                if nums[y] > nums[x - 1]:
                    nums[x - 1], nums[y] = nums[y], nums[x - 1]
                    break
        right = nums[x:]
        right.sort()
        nums[x:] = right
        return nums

if __name__ == '__main__':
    print(Solution().nextPermutation([1,2,2,1,3,2,4,3]))