# Definition for singly-linked list.
class ListNode(object):
    def __init__(self):
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        slowerNode = head
        fasterNode = head

        while(slowerNode is not None and fasterNode is not None and fasterNode.next is not None):
            slowerNode = slowerNode.next
            fasterNode = fasterNode.next.next

            if(slowerNode == fasterNode):
                return True
        return False

        