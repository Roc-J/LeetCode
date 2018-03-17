# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        for item in nums2:
            if len(nums1) == 0:
                return result
            if item in nums1:
                result.append(item)
                nums1.remove(item)

        return result

if __name__ == '__main__':
    print Solution().intersect([1, 2, 1], [1, 2, 2])
