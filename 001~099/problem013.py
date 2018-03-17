# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        val = 0
        mapper = dict()
        mapper['I'] = 1
        mapper['V'] = 5
        mapper['X'] = 10
        mapper['L'] = 50
        mapper['C'] = 100
        mapper['D'] = 500
        mapper['M'] = 1000

        for i in range(len(s)-1):
            if mapper[s[i]] >= mapper[s[i+1]]:
                val += mapper[s[i]]
            else:
                val -= mapper[s[i]]
        val += mapper[s[len(s)-1]]

        return val

if __name__ == '__main__':
    print Solution().romanToInt("IV")