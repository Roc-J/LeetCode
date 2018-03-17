# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = dict()
        count = 0
        flag = 0
        for item in s:
            if item not in result:
                result[item] = 1
            else:
                result[item] += 1
        for item in result.keys():
            if result[item] % 2 == 0:
                count += result[item]
            else:
                flag = 1
                count += (result[item] - 1)
        count += flag
        return count

if __name__ == '__main__':
    print Solution().longestPalindrome("bb")
