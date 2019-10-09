
class Solution {
    func reverseList(_ head: ListNode?) -> ListNode? {
        var preNode: ListNode? = nil
        var curNode: ListNode? = head

        while (curNode !== nil) {
            let nextNode = curNode!.next

            curNode!.next = preNode
            preNode = curNode
            curNode = nextNode
        }

        return preNode
    }
}
