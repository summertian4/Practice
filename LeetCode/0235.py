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
        # 搜索二叉树（BST），满足左子树所有节点 < 根节点 < 右子树所有节点 
        minn = min(p.val, q.val)
        maxn = max(p.val, q.val)
        if root is None:
            return None
        if minn <= root.val <= maxn:
            return root
        else:
            l = self.lowestCommonAncestor(root.left, p, q)
            r = self.lowestCommonAncestor(root.right, p, q)
            if l:
                return l
            if r:
                return r