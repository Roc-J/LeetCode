# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for item in nums:
            if item == 0:
                nums.remove(item)
                nums.append(0)

if __name__ == '__main__':
    print Solution().moveZeroes([1, 2, 0, 3, 5, 0, 4])
