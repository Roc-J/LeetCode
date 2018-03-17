# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        i = 0
        j = 0
        result = list()
        while i < len1 and j < len2:
            if nums1[i]<=nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
        while i < len1:
            result.append(nums1[i])
            i += 1
        while j < len2:
            result.append(nums2[j])
            j += 1
        length = len(result)
        print result
        if length % 2 == 0:
            return (result[length/2-1] + result[length/2])*1.0/2
        else:
            return result[length/2]

if __name__ == '__main__':
    print Solution().findMedianSortedArrays([1, 2], [3, 4, 5])