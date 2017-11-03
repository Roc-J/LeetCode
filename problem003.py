# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        maxLength = 1
        currLength = 0
        result = []
        for item in s:
            if item not in result:
                result.append(item)
                currLength += 1
            else:
                index = result.index(item)
                if index < len(result)-1:
                    result = result[(index+1):]
                else:
                    result = []
                result.append(item)
                currLength = len(result)
            if maxLength < currLength:
                maxLength = currLength

        return maxLength

if __name__ == '__main__':
    print Solution().lengthOfLongestSubstring("dvdf")