# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) < len(num2):
            temp = num2
            num2 = num1
            num1 = temp
        result = ''
        flag = 0
        for i in range(1, len(num1)+1):
            if i <= len(num2):
                result = str(((ord(num1[-i]) - ord('0')) + (ord(num2[-i]) - ord('0')) + flag) % 10) + result
                if (ord(num1[-i]) - ord('0')) + (ord(num2[-i]) - ord('0') + flag) > 9:
                    flag = 1
                else:
                    flag = 0
            else:
                result = str(((ord(num1[-i]) - ord('0')) + flag) % 10) + result
                if (ord(num1[-i]) - ord('0') + flag) > 9:
                    flag = 1
                else:
                    flag = 0
        if flag == 1:
            result = '1' + result
            return result
        else:
            return result

if __name__ == '__main__':
    print Solution().addStrings('9', '99')


