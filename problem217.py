# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        result = dict()
        for item in nums:
            if item not in result:
                result[item] = 1
            else:
                return True
        return False