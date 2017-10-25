# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while True:
            if val in nums:
                nums.pop(nums.index(val))
            else:
                break
        return len(nums)


if __name__ == '__main__':
    print Solution().removeElement([3, 2, 2, 1, 3], 2)