# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        global res, count
        res,count = 0,0
        def search(root, k) :
            if not root:
                return
            search(root.left, k)
            global count, res
            count += 1
            if count == k:
                res = root.val
            search(root.right, k)
        search(root, k)
        return res