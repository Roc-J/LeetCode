# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = dict()
        for item in nums:
            if item not in a.keys():
                a[item] = 1
            else:
                a[item] += 1
        result = sorted(a.iteritems(), key=lambda d: d[1], reverse=True)
        return result[0][0]



if __name__ == '__main__':
    print Solution().majorityElement([2,2,2,2,1,1])