class Stack(object):
    def __init__(self):
         self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return False
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = "([{"
        right = ")]}"
        stk = Stack()
    
        for i in range(0, s.__len__()):
            c = s[i]
            if left.find(c) != -1:
                stk.push(c)
            else:
                rightIndex = right.index(c)
                condition0 = stk.peek() == left[rightIndex]
                condition1 = stk.is_empty() == False
                if condition0 and condition1:
                    stk.pop()
                else:
                    return False
                
        return stk.is_empty()
        
s = Solution()

result = s.isValid("]")
print(result)
        