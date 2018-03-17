#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapper = {}
        mapper['2'] = ['abc']
        mapper['3'] = ['def']
        mapper['4'] = ['ghi']
        mapper['5'] = ['jkl']
        mapper['6'] = ['mno']
        mapper['7'] = ['pqrs']
        mapper['8'] = ['tuv']
        mapper['9'] = ['wxyz']

        result = []
        ans = []
        for item in digits:
            for letter in mapper[item]:
                for elem in letter:
                    if len(result) == 0:
                        ans.append(elem)
                    else:
                        for x in result:
                            ans.append(x+elem)
                result = ans
                ans = []
        return result

if __name__ == '__main__':
    print(Solution().letterCombinations('23456789'))

