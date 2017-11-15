# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = []
        for item in nums:
            if item not in result:
                result.append(item)
                if len(result) == 3:
                    break
        if len(result) <= 2:
            return max(result)
        print result
        for i in range(3, len(nums)):
            minNumber = min(result)
            if nums[i] not in result and nums[i] > minNumber:
                result.remove(minNumber)
                result.append(nums[i])

        return min(result)

if __name__ == '__main__':
    print Solution().thirdMax([1,2,2,5,3,5])
