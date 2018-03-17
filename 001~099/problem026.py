# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        idx = 0
        while True:
            if nums[idx] == nums[(idx+1)]:
                nums.pop(idx)
            else:
                idx += 1
            if idx >= len(nums)-1:
                break

        return len(nums)

if __name__ == '__main__':
    print Solution().removeDuplicates([1, 1])