# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        current = root
        # current 空，或者，current 是 p q 中的一个（找到）
        if not current or current.val in (p.val, q.val):
            return current
        
        left = self.lowestCommonAncestor(current.left, p, q)
        right = self.lowestCommonAncestor(current.right, p, q)
        
        # 同时满足，说明p/q分别属于这个节点左右子节点的某个子孙节点
        if left and right:
            return current
        
        current = left or right

        return current