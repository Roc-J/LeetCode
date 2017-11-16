# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = sum(nums)
        number1 = 0
        for i in range(len(nums)):
            if number1 == count-nums[i]-number1:
                return i
            number1 += nums[i]
        return -1

if __name__ == '__main__':
    print Solution().pivotIndex([1, 2, 3])
