# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)):
            num = target - nums[i]
            if num in nums[(i+1):]:
                j = nums[i+1:].index(num)
                result.append(i)
                result.append(j+i+1)
                return result
        return result

if __name__ == '__main__':
    print Solution().twoSum([2, 2, 3, 4], 4)
