# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True

        if len(s) % 2 == 1:
            return False
        flag = 0
        result = list()
        for item in s:
            if item in ['(', '[', '{']:
                result.append(item)
            if item == ')':
                if len(result) == 0:
                    return False
                if result.pop() == '(':
                    flag = 1
                else:
                    flag = 0
                    break
            if item == ']':
                if len(result) == 0:
                    return False
                if result.pop() == '[':
                    flag = 1
                else:
                    flag = 0
                    break
            if item == '}':
                if len(result) == 0:
                    return False
                if result.pop() == '{':
                    flag = 1
                else:
                    flag = 0
                    break

        if len(result) == 0 and flag == 1:
            return True
        else:
            return False


if __name__ == '__main__':
    print Solution().isValid("([])")