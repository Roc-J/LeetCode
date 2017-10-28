# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        maxinum = nums[0]
        result = 0
        for i in range(len(nums)):
            result += nums[i]
            if maxinum < result:
                maxinum = result
            if result < 0:
                result = 0

        return maxinum

if __name__ == '__main__':
    print Solution().maxSubArray([-2, -2, -2])