# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        result = dict()
        for i, item in enumerate(nums):
            if item not in result:
                result[item] = i
            else:
                if (i - result[item]) <= k:
                    return True
                else:
                    result[item] = i
        return False

if __name__ == '__main__':
    print Solution().containsNearbyDuplicate([1, 0, 1, 1], 1)