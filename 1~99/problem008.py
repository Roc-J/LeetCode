#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk


'''
atoi函数
atoi是把字符串转换成整数的一个函数
会扫描参数字符串，跳过前面的空白字符（例如空格，tab缩进）
'''
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        newStr = []
        for i in xrange(len(str)):
            if '0' <= str[i] <= '9' or (str[i] in ('+', '-') and i == 0):
                newStr.append(str[i])
            else:
                break
        if newStr in ([], ['+'], ['-']):
            return 0
        elif -2147483648 <= int(''.join(newStr)) <= 2147483647:
            return int(''.join(newStr))
        elif int(''.join(newStr)) > 2147483647:
            return 2147483647
        else:
            return -2147483648

if __name__ == '__main__':
    print(Solution().myAtoi('+5467876543234567876'))
