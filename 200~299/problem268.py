# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        for item in nums:
            sum += item
        count = len(nums) * (len(nums)+1) /2
        return count-sum

if __name__ == '__main__':
    print Solution().missingNumber([0, 1, 3])