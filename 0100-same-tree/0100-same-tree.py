# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if not p and not q:
            return True
        
        if not p and q:
            return False

        if p and not q:
            return False

        if p.val != q.val:
            return False
        
        left_same = self.isSameTree(p.left, q.left)
        right_same = self.isSameTree(p.right, q.right)

        if left_same and right_same:
            return True
        else:
            return False

            