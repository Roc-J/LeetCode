# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        for i in range(k):
            nums.insert(0, nums.pop())
        return nums

if __name__ == '__main__':
    print Solution().rotate([1, 2, 3, 4, 5, 6, 7], 6)