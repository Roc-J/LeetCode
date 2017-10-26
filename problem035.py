# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        flag = 0
        for i in range(len(nums)):
            if nums[i] < target:
                continue
            else:
                flag = 1
                return i
        if flag == 0:
            return len(nums)

if __name__ == '__main__':
    print Solution().searchInsert([1, 3, 5, 6], 0)
    # [1, 3, 5, 6], 5 → 2
    # [1, 3, 5, 6], 2 → 1
    # [1, 3, 5, 6], 7 → 4
    # [1, 3, 5, 6], 0 → 0