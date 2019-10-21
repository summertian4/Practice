class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = s.split(' ')
        res = ''
        for item in ans:
            value = self.reverseString(item)
            res = res + value + ' '
        return res.strip()
    
    def reverseString(self, s):
        arr = list(s)
        count = len(arr)
        for i in range(count - 1):
            value = arr.pop(0)
            arr.insert(count-i-1, value)
        reverseStr = ''.join(str(i) for i in arr)
        return reverseStr