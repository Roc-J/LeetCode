# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        total = [0] * (size+1)
        if size:
            total[1] = nums[0]
        for i in range(2, size+1):
            total[i] = max(total[i-1], total[i-2] + nums[i-1])
        return total[size]

if __name__ == '__main__':
    print Solution().rob([9, 8, 8, 1, 9])
