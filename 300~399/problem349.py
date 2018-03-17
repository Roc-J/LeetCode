# -*- coding:utf-8 -*-
# Author: Roc-J

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        for item in nums2:
            if item in nums1:
                result.append(item)
        return result

if __name__ == '__main__':
    print Solution().intersection([1, 2, 1], [])
