# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        result = dict()
        for item in s:
            if item not in result:
                result[item] = 1
            else:
                result[item] += 1

        for item in t:
            if item not in result:
                result[item] = 1
            else:
                result[item] += 1

        for item in t:
            if result[item] % 2 == 1:
                return item

if __name__ == '__main__':
    print Solution().findTheDifference("abcd", "abcda")