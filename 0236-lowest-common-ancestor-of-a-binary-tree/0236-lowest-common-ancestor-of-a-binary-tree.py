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

        if not root:
            return None

        if root.val == p.val:
            return p

        if root.val == q.val:
            return q

        left = self.lowestCommonAncestor(root.left, p, q)

        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        if left and not right:
            return left

        if not left and right:
            return right

        if not left and not right:
            return None
        
        