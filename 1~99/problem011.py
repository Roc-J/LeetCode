#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk


'''
容器，求一个最大值
将最大值设置为０，从俩边递进
'''
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        left, right = 0, len(height)-1
        while left <= right and left >= 0 and right <= len(height)-1:
            maxArea = max(maxArea, (right-left)*min(height[left], height[right]))
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        return maxArea

if __name__ == '__main__':
    print(Solution().maxArea([10, 1, 2, 3, 10, 5, 6]))