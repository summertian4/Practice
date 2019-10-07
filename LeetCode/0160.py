class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None

        headALen = self.getCount(headA)
        headBLen = self.getCount(headB)

        if headALen < headBLen:
            result = headBLen - headALen
            while result > 0:
                result -= 1
                headB = headB.next

        if headALen > headBLen:
            result = headALen - headBLen
            while result > 0:
                result -= 1
                headA = headA.next

        ha = headA
        hb = headB

        temp = None
        while ha is not None and hb is not None:
            if ha == hb:
                temp = ha
                break
            else:
                ha = ha.next
                hb = hb.next
            
        return temp

    def getCount(self, listNode):
        i = 1
        node = listNode
        while node.next is not None:
            i += 1
            node = node.next
        return i