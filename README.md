# Leetcode 题解

leetcode 是一个在线编程的算法题，使用python来进行结题。

## leetcode部分总结

1. Two Sum题目大意：给定一个整数数组，从中找出两个数的下标，使得它们的和等于一个特定的数字。可以假设题目有唯一解。

解题思路： 利用字典idxDict保存数字num到其下标idx的映射，遍历查找数字num与目标数target的“互补数”时，只需要查找idxDict[target-num]是否存在即可。

```
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        idxDict = dict()
        for idx, num in enumerate(nums):
            if target - num in idxDict:
                return [idxDict[target - num], idx]
            idxDict[num] = idx
```

2. Add Two Numbers 题目大意：给定两个链表分别代表两个非负整数。数位以倒序存储，就是高位在后，低位在前，并且每一个节点包含一位数字。将两个数字相加并以链表形式返回。

解题思路：主要考察链表操作和加法进位的基础知识。

```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        head = ListNode(0)
        l = head
        carry = 0
        while l1 or l2 or carry:
            sum, carry = carry, 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            if sum > 9:
                carry = 1
                sum -= 10
            l.next = ListNode(sum)
            l = l.next
        return head.next
```

3. Longest Substring Without Repeating Characters 题目大意：给定一个字符串，从中找出不含重复字符的最长子串的长度。例如，“abcabcbb”的不含重复字母的最长子串为“abc”，其长度为3。“bbbbb”的最长子串是“b”，长度为1 。

解题思路：

”滑动窗口法“，变量start和end分别记录子串的起点和终点，从左向右逐字符遍历原始字符串，每次将end+1；字典countDict存储当前子串中各字符的个数；当新增字符c的计数>1时，向右移动起点start，并将s[start]在字典中的计数-1，直到countDict[c]不大于1为止；更新最大长度。

```
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        ans, start, end = 0, 0, 0
        countDict = {}
        for c in s:
            end += 1
            countDict[c] = countDict.get(c, 0) + 1
            while countDict[c] > 1:
                countDict[s[start]] -= 1
                start += 1
            ans = max(ans, end - start)
        return ans
```

4. Median of Two Sorted Arrays 题目大意：有两个已经排序的数组，大小分别为m,n，找到这两个数组的中位数。

解题思路：

遍历一次，将两个排序的数组合并成一个数组，这个数组也是已经排好序的，根据数组大小求中位数。

```
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        i = 0
        j = 0
        result = list()
        while i < len1 and j < len2:
            if nums1[i]<=nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
        while i < len1:
            result.append(nums1[i])
            i += 1
        while j < len2:
            result.append(nums2[j])
            j += 1
        length = len(result)
        print result
        if length % 2 == 0:
            return (result[length/2-1] + result[length/2])*1.0/2
        else:
            return result[length/2]

if __name__ == '__main__':
    print Solution().findMedianSortedArrays([1, 2], [3, 4, 5])
```

5. Longest Palindromic Substring 题目大意：给定一个字符串s，找到该字符串的最大回文子字符串，假设字符串s长度不超过1000。

解题思路：还是遍历，不过要考虑是偶数还是奇数两种情况。从字符串分别向左，向右扩展字符串判断是不是回文；更新最大回文字符串的长度。

```
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def palindrome(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        ans = ''

        for i in range(len(s)):
            pal1 = palindrome(s, i, i)
            if len(pal1) > len(ans):
                ans = pal1
            pal2 = palindrome(s, i, i + 1)
            if len(pal2) > len(ans):
                ans = pal2

        return ans

if __name__ == '__main__':
    print(Solution().longestPalindrome("aabaaa"))
```

6. ZigZag Conversion 题目大意：在行数给定时，字符串“PAYPALISHIRING”的Z字形（zigzag）写法像这样：（使用等宽字体可以得到更好的显示效果）

   ```
   P   A   H   N
   A P L S I I G
   Y   I   R
   ```

   然后一行一行的读取：“PAHNAPLSIIGYIR”

   编写代码读入字符串以及行数，将字符串转化为其Z字形式：

   ```
   string convert(string text, int nRows);
   ```

   convert("PAYPALISHIRING", 3)应当返回“PAHNAPLSIIGYIR”。

解题思路：模拟题，使用长度为numRows的数组按行存储经过zigzag转化后的字母，最后将每一行的字母顺次拼接即可。

其实排序可以发现对应的下标是有规律的。字母下标与其所在行的对应关系。

```
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        result = []
        for i in range(numRows):
            flag = 1
            step = (numRows - 1) * 2
            step1 = (numRows - i - 1) * 2
            step2 = step - step1
            if i == 0 or i == numRows-1:
                j = i
                while j < len(s):
                    result.append(s[j])
                    j += step
            else:
                j = i
                while j < len(s):
                    result.append(s[j])
                    if flag == 1:
                        j += step1
                        flag = 0
                    else:
                        j += step2
                        flag = 1
        return "".join(result)

if __name__ == '__main__':
    print(Solution().convert("ABc", 2))
```

7. Reverse Integer 题目大意：给定一个32为整数，逆序输出

解题思路：32位，不能超出32位的整数范围

```
32位有符号整数范围
-2^32 - 2^32
'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            x = -x
            flag = 1
        else:
            flag = 0
        num2str = str(x)
        result = ''
        for item in num2str[::-1]:
            result += item
        result = int(result)
        number = result

        n = 31
        while n:
            result = result * 1.0/2
            n = n - 1
        if result > 1:
            return 0

        if flag == 1:
            number = -number
        return number

if __name__ == '__main__':
    print Solution().reverse(8463847412)
```

8. String to Integer(atoi) 题目大意：实现atoi函数将字符串转换为整数。

   atoi的要求：

   函数首先尽可能多的丢弃空白字符，直到发现第一个非空字符位为止。接着从这个字符开始，读入一个可选的正负号，然后尽可能多的读入数字，最后将它们解析成数值。

   字符串中在合法数字后可以包含额外的非法字符，对于这些字符只需丢弃即可。

   如果字符串的非空字符不是一个有效的整数，或者，当字符串为空或者只包含空白字符时，不需要执行转换。

   如果不能够执行有效的转化则返回0.如果得到的数值超出了整数范围，返回INT_MAX(2147483647)或者INT_MIN(-2147483648)

```
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
```

9. Palindrome Number 题目大意：判断一个整数是否是回文的

解题思路：把负数排除了

```
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        num2str = str(x)
        left = ''
        right = ''
        for item in num2str:
            left += item
        for item in num2str[::-1]:
            right += item

        if left == right:
            return True
        else:
            return False

if __name__ == '__main__':
    print Solution().isPalindrome(-2147447412)
```

11.Container With Most Water 题目：包含最多的水

题目大意：是给定整形数组a，(i, ai)表示坐标点，这些坐标点向x轴作垂直的线。找到两条线，使其和x轴共同构成的容器，可以装下最多的水。（注意，不允许倾斜容器）

简单直接的思路是两层循环遍历每组可能的情况，时间复杂度O(n2)。可以进一步优化，采用两个指针l和r，初始化分别指向数组的两端，然后在向中间移动找到最大容量。如果l指向的数字小，则l需要右移才有可能获得更大容量，因为此时如果左移r，得到的容量肯定比左移r之前的容量小（高度已经被较小的l限制住了）。如果r指向的数字小，则需要左移r。这样，当l和r相遇的时候，最大的容量就是我们需要的。

时间复杂度：O(n)

空间复杂度：O(1)

```
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        left, right = 0, len(height-1)
        while left <= right and left >=0 and right <= len(height)-1:
        	maxArea = max(maxArea, (right-left)*min(height[left], height[right]))
        	if height[left] >= height[right]:
        		right -= 1
        	else:
        		left += 1
        return maxArea
```

15. 3Sum

与Two Sum和 4 Sum类似，算法如下：

1、先对数组nums进行排序

2、对数组中的每个元素下表i，begin=i+1， end=length-1，sum = nums[i] + nums[begin] + nums[end]

​               sum == 0, 将三个元素组成vector，插入到结果vector中， begin++

​               sum < 0. begin++

​               sum >0  end--

要注意对重复元素的处理，避免产生重复元素。

​      nums[i] == nums[i-1]，

​     nums[begin] == nums[begin-1]

​     nums[end] == nums[end+1]

```
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        size = len(nums)
        ans = []
        if size <= 2:
            return ans
        nums.sort()
        i = 0
        while i < size -2:
            tmp = 0 - nums[i]
            j = i + 1
            k = size -1
            while j < k:
                if nums[j] + nums[k] < tmp:
                    j += 1
                elif nums[j] + nums[k] > tmp:
                    k -= 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k:
                        if nums[j] != nums[j - 1]:
                            break
                        if nums[k] != nums[k + 1]:
                            break
                        j += 1
                        k -= 1
            i += 1
            while i < size - 2:
                if nums[i] != nums[i - 1]:
                    break
                i += 1
        return ans
```

16. 3Sum Closest 

题意：给定一个数组和目标元素，找出数组中的3个元素使其和最接近目标元素。

思路: 首先对给定的数组进行排序，然后从0到数组元素长度len-2开始循环，对于每层循环，定义两个指针一个left指向i+1,right指向数组的尾部，然后开始判断i,left和start指向的元素之和是否更接近给定的元素，如果接近则更新，然后判断3个元素的和是大于给定的元素还是小于给定的元素，大于的话left指针加1，小于的话right指针减1；

```
import sys
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        size = len(nums)
        ans = []
        if size <= 2:
            return ans
        nums.sort()
        i = 0
        distance = sys.maxint
        for i in range(size-2):
            j = i + 1
            k = size - 1
            while j < k:
                count = nums[i] + nums[j] + nums[k]
                diff = abs(count - target)
                if diff < distance:
                    distance = diff
                    result = count
                if count < target:
                    j += 1
                else:
                    k -= 1
        return result
```

