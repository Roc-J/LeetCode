#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

'''
第一个的每一位和下面的相乘，加到对应的位置
第二次循环，从第一个数加一位进行相乘
'''
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        product = [0] * (len(num1)+len(num2))
        pos = len(product) - 1

        for n1 in reversed(num1):
            tempos = pos
            for n2 in reversed(num2):
                product[tempos] += int(n1)*int(n2)
                product[tempos-1] += product[tempos]/10
                product[tempos] %= 10
                tempos -= 1
            pos -= 1

        curr = 0
        while curr < len(product)-1 and product[curr] == 0:
            curr += 1

        return ''.join(map(str, product[curr:]))



if __name__ == '__main__':
    print(Solution().multiply('123', '456'))