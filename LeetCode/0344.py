class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        count = len(s)
        for i in range(count - 1):
            value = s.pop(0)
            s.insert(count-i-1, value)