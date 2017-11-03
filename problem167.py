# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        low = 0
        high = len(numbers) -1
        while True:
            if numbers[low] + numbers[high] > target:
                high -= 1
            elif numbers[low] + numbers[high] < target:
                low += 1
            else:
                return [low+1, high+1]

if __name__ == '__main__':
    print Solution().twoSum([2,3,4], 6)