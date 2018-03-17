# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1 = nums1[:m]
        nums2 = nums2[:n]
        i = 0
        j = 0
        if m == 0:
            while j < n:
                nums1.append(nums2[j])
                j += 1
        else:
            while True:
                if j == n:
                    break
                if (i-j) >= m:
                    nums1.append(nums2[j])
                    j += 1
                else:
                    if nums1[i] > nums2[j]:
                        nums1.insert(i, nums2[j])
                        i += 1
                        j += 1
                    else:
                        i += 1


        return nums1

if __name__ == '__main__':
    print Solution().merge([0], 0, [1], 1)