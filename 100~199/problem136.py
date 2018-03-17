# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = 0
        for item in nums:
            num ^= item
        return num

if __name__ == '__main__':
    print Solution().singleNumber([2, 2, 1, 0, 1])